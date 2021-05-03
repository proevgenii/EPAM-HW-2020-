# Some imports here

import asyncio
import json
from concurrent.futures import ThreadPoolExecutor
from itertools import chain

import pandas as pd
import requests
from aiohttp import ClientSession
from bs4 import BeautifulSoup

# Main url to parse
url = "https://markets.businessinsider.com/index/components/s&p_500?p="


# Parse 10 main pages as text
async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()


async def get_main_pages():
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for i in range(1, 11):
            url = f"https://markets.businessinsider.com/index/components/s&p_500?p={i}"
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        return responses


# loop = asyncio.get_event_loop()
# future = asyncio.ensure_future(run())
# main_pages = loop.run_until_complete(future)  # Получаем 10 главных страаниц сайта


# Company names
def get_company_names(main_pages):
    comp_names = []
    soup = (
        BeautifulSoup(main_pages, "html.parser")
        .find(class_="table-small")
        .find_all("a")
    )
    for s in soup:
        comp_names.append(s.get("title"))  # Получаем имена компаний с главных страниц
    return comp_names


# Links for every company subpage
def get_sub_pages_links(main_pages):
    sub_pages = []
    soup = (
        BeautifulSoup(main_pages, "html.parser")
        .find(class_="table-small")
        .find_all("a")
    )
    for s in soup:
        sub_pages.append(s.get("href"))
    return sub_pages


# Так же как для 10 главных страниц, спарсим страницы каждой компании и сохраним в переменную
async def get_sub_pages():
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for i in sub_pages:
            url = f"https://markets.businessinsider.com{i}"

            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        return responses


# Function to get usd course
def get_usd_course():
    request = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    soup = BeautifulSoup(request.text, "lxml").find(id="R01235").value
    return float((soup.text).replace(",", "."))


usd_course = get_usd_course()


# Function to define current price in RUB.
def get_prices(sub_pages_texts):
    prices = []
    soup = BeautifulSoup(sub_pages_texts, "html.parser").find(
        class_="price-section__current-value"
    )
    for s in soup:
        prices.append(float(s.strip().replace(",", "")) * get_usd_course())
    return prices


# Function to get company code
def get_company_code(sub_pages_texts):
    codes = []

    soup = BeautifulSoup(sub_pages_texts, "html.parser").find(
        "span", class_="price-section__category"
    )
    codes.append(soup.text.replace("Stock , ", "").strip())
    return codes


# Function to get P/E ratio
def get_p_e_ratio(sub_pages_texts):
    p_e_ratio = []
    soup = (
        BeautifulSoup(sub_pages_texts, "html.parser")
        .find("div", class_="snapshot")
        .find_all(class_="snapshot__data-item")
    )
    for s in soup:
        if s.find(class_="snapshot__header", text="P/E Ratio"):
            p_e_ratio.append(s.text[:11].strip())
            return p_e_ratio
    p_e_ratio.append(None)
    return p_e_ratio


# Function to get year growth or falling prices
def get_year_growth(main_pages):
    growth_perc = []
    table = BeautifulSoup(main_pages, "html.parser").find(class_=("table-small"))
    for rows in table.find_all("tr")[1:]:
        growth_perc.append(
            rows.find_all(class_="text-right")[6]
            .find_all(class_=("colorRed", "colorGreen"))[1]
            .text
        )
    return growth_perc


# Function that calculate potential profit
# if the company's shares were bought for 52 weeks Low and were sold at 52 Week High
def get_potential_profit(sub_pages_texts):
    profit = []
    try:
        week_high = (
            BeautifulSoup(sub_pages_texts, "html.parser")
            .find(class_="snapshot__highlow-container")
            .find(class_="snapshot__highlow")
            .find_all(
                "div",
                class_=(
                    "snapshot__data-item snapshot__data-item--small snapshot__data-item--right",
                    "snapshot__data-item snapshot__data-item--small",
                ),
            )
        )

        low = float(week_high[0].text[:15].strip().replace(",", ""))
        high = float(week_high[1].text[:15].strip().replace(",", ""))
        profit.append((high - low) * usd_course)
    except IndexError:
        profit.append(None)
    except AttributeError:
        profit.append(None)
    return profit


# SAVING RESULTS
def get_most_ten(name_of_file, datafr, sort_by, ascending=True):
    """
    :param name_of_file: file name where the result will be saved
    :param datafr: Pandas DataFrame according to which the sorting will be performed
    :param sort_by: the name of the column to be sorted by
    """
    df_most = datafr.sort_values(by=[f"{sort_by}"], ascending=ascending)
    result = df_most[:10].to_json(orient="records")
    parsed = json.loads(result)
    with open((name_of_file), "w") as f:
        json.dump(parsed, f)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_main_pages())
    main_pages = loop.run_until_complete(future)  # Получаем 10 главных страаниц сайта

    # Получаем названия компаний и ссылки на их страницы
    with ThreadPoolExecutor(max_workers=10) as pool:
        comp_names = list(chain.from_iterable(pool.map(get_company_names, main_pages)))
        sub_pages = list(chain.from_iterable(pool.map(get_sub_pages_links, main_pages)))

    # Получаем страницы всех компаний
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_sub_pages())
    sub_pages_texts = loop.run_until_complete(future)

    # Запускаем вычисление всех необходимых по заданию функий
    with ThreadPoolExecutor(max_workers=100) as pool:
        potential_profit = list(
            chain.from_iterable(pool.map(get_potential_profit, sub_pages_texts))
        )
        year_growth = list(chain.from_iterable(pool.map(get_year_growth, main_pages)))
        p_e_ratio = list(chain.from_iterable(pool.map(get_p_e_ratio, sub_pages_texts)))
        price = list(chain.from_iterable(pool.map(get_prices, sub_pages_texts)))
        company_code = list(
            chain.from_iterable(pool.map(get_company_code, sub_pages_texts))
        )

    # Cохранение результатов
    df = pd.DataFrame(
        {
            "Name": comp_names,
            "Code": company_code,
            "Price, RUB": price,
            "P/E": p_e_ratio,
            "Year growth, %": year_growth,
            "Potential profit, RUB": potential_profit,
        }
    )

    # 1. Топ 10 компаний с самими дорогими акциями в рублях.
    get_most_ten("most_expensive.json", df, "Price, RUB", ascending=True)

    # 2. Топ 10 компаний с самым низким показателем P/E.
    get_most_ten("min_p_e_value.json", df, "P/E", ascending=False)

    # 3. Топ 10 компаний, которые показали самый высокий рост за последний год
    get_most_ten("max_year_growth.json", df, "Year growth, %", ascending=False)

    # 4. Топ 10 комппаний, которые принесли бы наибольшую прибыль,
    # если бы были куплены на самом минимуме и проданы на самом максимуме за последний год.
    get_most_ten("most_valid.json", df, "Potential profit, RUB", ascending=False)

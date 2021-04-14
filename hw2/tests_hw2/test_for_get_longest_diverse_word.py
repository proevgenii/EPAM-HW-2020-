import pytest

from hw2.hw1 import get_longest_diverse_words


@pytest.fixture
def file_creater():
    file = open("test.txt", "w")
    file.write("abcdefgh abcdef abcdeeeee")
    file.close()


@pytest.mark.parametrize(
    ["path", "expected_result"],
    [
        ("test.txt", ["abcdefgh", "abcdef", "abcdeeeee"]),
        (
            "data.txt",
            [
                "Verfassungsverletzungen",
                "politischstrategischen",
                "Wiederbelebungsübungen",
                "Werkstättenlandschaft",
                "Geschichtsphilosophie",
                "zoologischpolitischen",
                "Werkstättenlandschaft",
                "Entscheidungsschlacht",
                "Selbstbezichtigungen",
                "Geschichtsunterricht",
                "Gewissenserforschung",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(path: str, expected_result: tuple):
    assert get_longest_diverse_words(path) == expected_result

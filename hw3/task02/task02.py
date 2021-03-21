import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def function_for_parallelize_calculating_sum():
    start_time = time.time()
    with Pool(28) as p:
        result = sum(p.map(slow_calculate, range(500)))
    return int((time.time() - start_time))

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


def f():

    start_time = time.time()
    if __name__ == "__main__":
        with Pool(28) as p:
            summ = sum(p.map(slow_calculate, range(500)))
            return int((time.time() - start_time))

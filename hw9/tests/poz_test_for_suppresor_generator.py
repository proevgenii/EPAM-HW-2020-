import pytest

from hw9.hw2 import supressor


@pytest.mark.parametrize(
    "exc_to_suppr,  exc_to_raise",
    [(ValueError, ValueError), (IndexError, IndexError), (ImportError, ImportError)],
)
def test_for_suppressor_gen(exc_to_suppr, exc_to_raise):
    with supressor(exc_to_suppr):
        raise exc_to_raise

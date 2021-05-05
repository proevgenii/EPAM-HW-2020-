import pytest

from hw9.hw2 import supressor


@pytest.mark.parametrize(
    "exc_to_suppr,  exc_to_raise", [(ValueError, IndexError), (IndexError, ValueError)]
)
def test_for_suppressor_gen(exc_to_suppr, exc_to_raise):
    with pytest.raises(exc_to_raise):
        with supressor(exc_to_suppr):
            raise exc_to_raise

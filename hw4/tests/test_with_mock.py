from unittest.mock import patch

from hw4.task_2_mock_input import count_dots_on_i


def test_counts_dots():
    with patch("urllib.request.urlopen") as fake_request:
        fake_request.return_value = "iiii"
        assert count_dots_on_i("wq") == 4

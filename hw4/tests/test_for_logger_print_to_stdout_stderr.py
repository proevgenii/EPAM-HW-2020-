from hw4.task_3_get_print_output import my_precious_logger


def test_output_my_precious_logger(capsys):
    my_precious_logger("OK")
    out, err = capsys.readouterr()
    assert out == "OK\n"
    assert err == ""

    my_precious_logger("error: file not found")
    out, err = capsys.readouterr()
    assert out == ""
    assert err == "error: file not found\n"

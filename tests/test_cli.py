from calculator.__main__ import main


def test_add_command_prints_sum(capsys) -> None:
    exit_code = main(["add", "2", "3"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip() == "5"

from python_hub.cli.app import main


def test_version_command(capsys) -> None:
    exit_code = main(["--version"])
    output = capsys.readouterr().out
    assert exit_code == 0
    assert "python-hub" in output


def test_catalog_json_command(capsys) -> None:
    exit_code = main(["catalog", "list", "--json"])
    output = capsys.readouterr().out
    assert exit_code == 0
    assert '"code-development"' in output
    assert '"documentation"' in output


def test_locales_command(capsys) -> None:
    exit_code = main(["locales"])
    output = capsys.readouterr().out
    assert exit_code == 0
    assert "English" in output
    assert "Persian" in output


def test_help_is_returned_without_a_command(capsys) -> None:
    exit_code = main([])
    output = capsys.readouterr().out
    assert exit_code == 0
    assert "usage:" in output

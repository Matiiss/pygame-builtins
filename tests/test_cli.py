import subprocess
import sys

import tomlkit


def create_python_process_with_cli(*args):
    return subprocess.Popen(
        [sys.executable, "-m", "pygame_builtins", *args],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def read_pyproject_toml():
    try:
        with open("pyproject.toml") as file:
            return file.read()
    except FileNotFoundError:
        return ""


def write_pyproject_toml(content):
    with open("pyproject.toml", "w") as file:
        file.write(content)


def test_invalid_aliases():
    original_content = read_pyproject_toml()
    try:
        for invalid_identifier in ["def", " ", "class", " x", "123", ".", "abc "]:
            assert create_python_process_with_cli("-a", invalid_identifier).wait() != 0
            assert (
                create_python_process_with_cli("-a", f"{invalid_identifier}").wait()
                != 0
            )
            assert (
                create_python_process_with_cli("--alias", invalid_identifier).wait()
                != 0
            )
            assert (
                create_python_process_with_cli(
                    "--alias", f"{invalid_identifier}"
                ).wait()
                != 0
            )
    except Exception as e:
        write_pyproject_toml(original_content)
        raise e
    else:
        write_pyproject_toml(original_content)


def test_valid_aliases_in_pyproject_toml():
    def check_pyproject_toml_alias(value):
        with open("pyproject.toml") as file:
            data = tomlkit.load(file)
            return data["pygame-builtins"]["alias"] == value

    original_content = read_pyproject_toml()
    try:
        for valid_identifier in [
            "pg",
            "pygame",
            "class_",
            "gamelib",
            "pygame_ce",
            "random",
            "abc",
        ]:
            assert create_python_process_with_cli("-a", valid_identifier).wait() == 0
            assert check_pyproject_toml_alias(valid_identifier)

            assert (
                create_python_process_with_cli("-a", f"{valid_identifier}").wait() == 0
            )
            assert check_pyproject_toml_alias(valid_identifier)

            assert (
                create_python_process_with_cli("--alias", valid_identifier).wait() == 0
            )
            assert check_pyproject_toml_alias(valid_identifier)

            assert (
                create_python_process_with_cli("--alias", f"{valid_identifier}").wait()
                == 0
            )
            assert check_pyproject_toml_alias(valid_identifier)
    except Exception as e:
        write_pyproject_toml(original_content)
        raise e
    else:
        write_pyproject_toml(original_content)

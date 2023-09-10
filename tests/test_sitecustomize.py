import os
import subprocess
import sys

ENV_VAR_NAME = "PYGAME_BUILTINS_ALIAS"


def create_python_process_with_code(code):
    return subprocess.Popen(
        [sys.executable, "-c", f"{code}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def read_pyproject_toml():
    try:
        with open("pyproject.toml") as file:
            return file.read()
    except FileNotFoundError:
        return ""


def test_default_behaviour():
    if ENV_VAR_NAME in os.environ:
        del os.environ[ENV_VAR_NAME]

    process = create_python_process_with_code("pygame")

    assert process.wait() == 0


def test_pygame_alias():
    os.environ[ENV_VAR_NAME] = "pygame"
    process = create_python_process_with_code("pygame")
    assert process.wait() == 0


def test_pg_alias():
    os.environ[ENV_VAR_NAME] = "pg"
    process = create_python_process_with_code("pg")
    assert process.wait() == 0

    process = create_python_process_with_code("pygame")
    assert process.wait() != 0


def test_pg_from_pyproject_toml():
    if ENV_VAR_NAME in os.environ:
        del os.environ[ENV_VAR_NAME]
    original_content = read_pyproject_toml()

    try:
        with open("pyproject.toml", "w") as file:
            file.write('[pygame-builtins]\nalias = "pg"')

        process = create_python_process_with_code("pg")
        assert process.wait() == 0

        process = create_python_process_with_code("pygame")
        assert process.wait() != 0
    except Exception as e:
        with open("pyproject.toml", "w") as file:
            file.write(original_content)
        raise e
    else:
        with open("pyproject.toml", "w") as file:
            file.write(original_content)

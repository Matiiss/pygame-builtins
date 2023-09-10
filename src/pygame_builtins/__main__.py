import argparse
import keyword

import tomlkit

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--alias", nargs="?", const="")
arg_namespace = parser.parse_args()

if arg_namespace.alias is not None:
    alias = arg_namespace.alias or "pygame"
    if not alias.isidentifier() or keyword.iskeyword(alias):
        print(
            "ValueError: given alias is either not a valid identifier or a reserved keyword"
        )
        raise SystemExit(1)

    with open("pyproject.toml") as file:
        data = tomlkit.load(file)
    try:
        with open("pyproject.toml", "w") as file:
            table = tomlkit.table()
            table.add("alias", alias)
            data["pygame-builtins"] = table
            tomlkit.dump(data, file)
    except Exception as e:
        with open("pyproject.toml", "w") as file:
            tomlkit.dump(data, file)
        raise e

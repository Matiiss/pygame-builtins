import builtins
import contextlib
import io
import os

import tomlkit

with contextlib.redirect_stdout(io.StringIO()):
    import pygame

alias = "pygame"

try:
    with open("pyproject.toml") as config:
        data = tomlkit.load(config)
        alias = data.get("pygame-builtins", {}).get("alias", alias)
except FileNotFoundError:
    pass

alias = os.environ.get("PYGAME_BUILTINS_ALIAS", alias)

setattr(builtins, alias, pygame)

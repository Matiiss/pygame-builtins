import builtins
import contextlib
import io

with contextlib.redirect_stdout(io.StringIO()):
    import pygame

builtins.pygame = pygame

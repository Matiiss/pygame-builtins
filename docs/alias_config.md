# Alias configuration

Some of you obviously may want to change the name to say `pg` as in to simulate
`import pygame as pg`. This can be done in a couple of ways.

## Using `pyproject.toml`
If you already have a `pyproject.toml` file in the root of your project, you can
simply add this as another configuration option to it.
```
[pygame-builtins]
alias = "pg"  # or any other valid, unreserved identifier
```

## Using the CLI
Suppose you don't have a `pyproject.toml` or you simply want to use the CLI,
you can use this command (both `-a` and `--alias` are a valid flag)
```
python -m pygame_builtins -a pg
```
Keep in mind that while running this your cwd should be your root directory.
If you already have a `pyproject.toml`, it will simply add the above mentioned table
to the end of that file. If you don't have a `pyproject.toml` file, it will create
one for you and add the above mentioned table to it.

## Using environment variables
Additionally it is possible to set an environment variable `PYGAME_BUILTINS_ALIAS` to
a value you would want to use as an alias. On Windows you can use `set` and on unix
systems use `export` to set it. Here is a Windows example:
```
set PYGAME_BUILTINS_ALIAS=pg
```

This will override the value in the `pyproject.toml` file during runtime, the value
in the file will remain unchanged.

# pygame-builtins
Adds pygame(-ce) to `builtins` so you can use it without importing it.

## Installation
```
pip install git+https://github.com/Matiiss/pygame-builtins
```

## Usage
By default the name is `pygame`, you can however, configure an alias to use instead, see below.
You can just use the name `pygame` in your environment freely, like any other built-in, for example, `int` or `str`.

## Alias configuration
You can simply run
```
python -m pygame_builtins --alias pg
```
It will create a `pyproject.toml` file in the cwd if it doesn't exist already
and add a config table for the tool to use during runtime to determine the alias.
You can read more in detail about configuring the alias [here](docs/alias_config.md).

## Rationale
What?

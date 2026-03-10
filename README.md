# Calculator

Minimal Python calculator project using a `src/` layout.

## Setup

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run the CLI

```bash
python -m calculator add 2 3
```

Expected output:

```text
5
```

## Run checks locally

```bash
ruff format --check .
ruff check .
pytest
```

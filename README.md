# mini-calc

A simple command-line calculator written in Python. It supports basic arithmetic operations and a Celsius-to-Fahrenheit conversion, with clean input validation and user-friendly error messages.

## Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplicaton (`*`)
- Division (`/`)
- Celsius -> Fahrenheit conversation (`f`)

## Installation

1. Install uv if you haven't already:

```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

2. Clone the repository:

```bash
git clone dbozbay/mini-calc
cd mini-calc
```

3. Install dependencies:

```bash
uv sync
```

## Usage

Run the program from the command line:

```bash
uv run main.py
```

You will be prompted to:

1. Enter the first number
2. Enter a mode (`+`, `-`, `*`, `/`, or `f`)
3. Enter a second number (unless using `f` mode)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


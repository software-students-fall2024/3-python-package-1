# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.


# PyFunBox

[![log github events](https://github.com/software-students-fall2024/3-python-package-1/actions/workflows/event-logger.yml/badge.svg)](https://github.com/software-students-fall2024/3-python-package-1/actions/workflows/event-logger.yml)


PyFunBox is a fun Python package that brings joy to developers with jokes, ASCII art, emojis, and random facts! This lighthearted package is designed to make coding sessions more enjoyable by offering humorous and entertaining features.


## Features

1. **Joke Generator**:
   - Returns a random programming joke.
   ```python
   from pyfunbox import joke
   print(joke())
   ```

2. **ASCII Art**:
   - Converts a string into ASCII art.
   ```python
   from pyfunbox import ascii_art
   print(ascii_art("Hello"))
   ```

3. **Emojiify Text**:
   - Replaces words in a string with emojis.
   ```python
   from pyfunbox import emojiify
   print(emojiify("I am happy and I love to code!"))
   ```

4. **Random Facts**:
   - Returns a random fact about a given topic.
   ```python
   from pyfunbox import random_fact
   print(random_fact("python"))
   ```

## Installation

Install PyFunBox from PyPI:
```bash
pip install pyfunbox
```


## Example Usage

Here's an example script demonstrating all functions in the package:

See the [example.py](example.py)

## Contributing

Developers are welcome to contribute to this project. Follow these steps to set up your environment and contribute:

1. **Clone the repository**:
   cd pyfunbox

2. **Set up the virtual environment**:
   ```bash
   pipenv install --dev
   pipenv shell
   ```

3. **Run tests to validate functionality**:
   ```bash
   pipenv run pytest
   ```

4. **Make your changes**:

5. **Create a pull request**:
   - Push your changes and open a pull request to the `main` branch.
   - Request a review from another contributor.


## Development Workflow

To build, test, and distribute the package:

1. **Run Tests**:
   ```bash
   pipenv run pytest
   ```

2. **Build the Package**:
   ```bash
   pipenv run python -m build
   ```

3. **Upload to PyPI**:
   ```bash
   pipenv run twine upload dist/*
   ```

---

## Links

- **PyPI Package**: [PyFunBox on PyPI](https://pypi.org/project/pyfunbox/)
- **GitHub Repository**: [GitHub Repository](https://github.com/software-students-fall2024/3-python-package-1/pyfunbox)

---

## Team Members

- [FinnickL](https://github.com/FinnickL)

---

## Environment Configuration

This project does not require any database or `.env` files. However, to use the package locally:

1. Set up a virtual environment:
   ```bash
   pipenv install
   pipenv shell
   ```

2. Build and test the package as needed.

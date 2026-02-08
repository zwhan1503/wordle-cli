# 🎲 Wordle CLI

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Created by zwhan

## Introduction

Play the popular word game **[Wordle](https://www.nytimes.com/games/wordle/index.html)** right inside of your terminal!

Built with Python using [click](https://github.com/pallets/click) and [rich](https://github.com/Textualize/rich) modules.

## 🎥 Demo

https://github.com/user-attachments/assets/1e9ff77a-25df-43bc-b48f-e43b2d9f19a5

## ✨ Features

- Over 5,700+ words to play from, credit to [@darkermango/5-Letter-words](https://github.com/darkermango/5-Letter-words) for the amazing word list
- Unlimited plays as well as offline play
- Cross platform compatibility (Linux/Windows/MacOS)

## 📦 Installation

### Requirements

Before installing, ensure that you have:
- Python 3.8 or higher
- [pip](https://pypi.org/project/pip/) or [pipx](https://github.com/pypa/pipx)

### Method 1: Using pipx (Recommended)
[pipx](https://github.com/pypa/pipx) is the recommended way to install CLI applications:

```bash
# If you haven't installed pipx
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Restart your terminal, then install wordle-cli
pipx install git+https://github.com/zwhan1503/wordle-cli.git
```

### Method 2: Using pip 

```bash
# Install directly with pip
pip install git+https://github.com/zwhan1503/wordle-cli.git

# Or install for your user only (no sudo required)
pip install --user git+https://github.com/zwhan1503/wordle-cli.git
```

### Verify Installation

After installation, verify that the programn works by running wordle in the terminal:

```bash
# Check if wordle-cli is available
wordle --help

# Should output something like this:
# Usage: wordle [OPTIONS] COMMAND [ARGS]...
#  Wordle CLI - Guess the 5-letter word!
# Options:
#  --help  Show this message and exit.
# Commands:
#  play  Play Wordle in your terminal! (random word)
```

## 🎮 Usage

### Start the game
To play wordle-cli, run this command in the terminal:
```bash
wordle play
```

## Acknowledgments
- Credits to [@darkermango/5-Letter-words](https://github.com/darkermango/5-Letter-words) for the amazing word list

## License
This project iss licensed under the [MIT LICENSE](https://opensource.org/license/mit). See the [LICENSE](https://github.com/zwhan1503/wordle-cli/blob/main/LICENSE) for more details.

⭐ If you enjoy this project, please give it a star on GitHub




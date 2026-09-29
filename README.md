<div align="center">

# 💰 KBC Mini Project

### A "Kaun Banega Crorepati"-style quiz game for your terminal.

Answer up to 21 questions, climb the prize ladder from ₹1,000, and walk away whenever you like.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Type](https://img.shields.io/badge/Type-CLI%20Game-8A2BE2?style=for-the-badge)](#how-to-play)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

[![Last commit](https://img.shields.io/github/last-commit/HarshCoder1122/KBC-mini-project?style=flat-square)](https://github.com/HarshCoder1122/KBC-mini-project/commits/main)
[![Issues](https://img.shields.io/github/issues/HarshCoder1122/KBC-mini-project?style=flat-square)](https://github.com/HarshCoder1122/KBC-mini-project/issues)

</div>

## Table of contents

- [Overview](#overview)
- [How to play](#how-to-play)
- [Getting started](#getting-started)
- [Sample session](#sample-session)
- [How it works](#how-it-works)
- [Project structure](#project-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Overview

The game asks 21 multiple-choice questions on general knowledge, Indian culture, science and pop culture. Each question has four options and one correct answer. Prizes double roughly at each level, ending at ₹7,00,00,000.

## How to play

- Type `1`–`4` to pick an answer.
- Type `0` to **quit** and keep what you have won so far.
- A wrong answer ends the game and shows the correct one.

## Getting started

No dependencies. You only need Python 3.

```bash
git clone https://github.com/HarshCoder1122/KBC-mini-project.git
cd KBC-mini-project
python sourcecode.py
```

## Sample session

```text
Question For Rs. 1000
Which city is known as the Pink City of India?
1.Banglore             2.Mysore
3.Jaipur             4.Kochi
Press 0 to Quit or Enter the Answer No.: 3
Correct Answer, You won Rs. 1000
```

## How it works

- Questions live in a list of lists: `[question, opt1, opt2, opt3, opt4, correct_index]`.
- A parallel `levels` list holds the prize for each question.
- A `for` loop walks through the questions, reads input, compares it with the stored answer, and updates `money_won`.

## Project structure

```text
KBC-mini-project/
├── sourcecode.py   # Full, tested game (run this one)
├── main.py         # Scratch file used while trying out the logic
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
└── SECURITY.md
```

## Roadmap

- [ ] Validate non-numeric input instead of crashing
- [ ] Add lifelines (50-50, audience poll)
- [ ] Load questions from a JSON file
- [ ] Shuffle and sample questions each game
- [ ] Add safe checkpoints (₹10,000 and ₹3,20,000)

## Contributing

New questions, bug fixes, and features are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

Released under the [MIT License](LICENSE).

<div align="center"><sub>Built by <a href="https://github.com/HarshCoder1122">Harsh</a>.</sub></div>

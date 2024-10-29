# Superheroes Dueler

Welcome to **Superheroes Dueler**, a Python-based battle simulation game where players can create their own superhero teams and battle against each other using abilities, weapons, and armor. 

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features
- Create custom heroes with unique abilities, weapons, and armor.
- Form two teams and engage in simulated battles.
- Track statistics such as kills and deaths for each hero.
- Revive heroes for subsequent battles.

## Installation
To get started with the Superheroes Dueler, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/mrochelle23/superheroes-dueler.git
   ```

2. Navigate into the project directory:
   ```bash
   cd superheroes-dueler
   ```

3. Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

4. Install any necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   *(Note: If there are no specific dependencies, you can skip this step.)*

## Usage
1. Run the game by executing:
   ```bash
   python arena.py
   ```

2. Follow the prompts to create your heroes, add abilities, weapons, and armor, and then battle against another team.

3. After each battle, view the statistics and choose whether to play again.

## Project Structure
The project consists of the following files:

- `arena.py`: Main game logic and arena setup.
- `ability.py`: Class definition for abilities and their damage calculations.
- `armor.py`: Class definition for armor and its blocking mechanics.
- `hero.py`: Class definition for heroes, including health and combat mechanics.
- `weapon.py`: Class definition for weapons and their attack values.
- `team.py`: Class to manage teams of heroes.
- `dog.py`: Example class demonstrating basic object-oriented programming principles.
- `animal.py`: Example class showing inheritance in Python.
- `hero_test.py`: Unit tests for the ability, weapon, and hero classes.

## Testing
The project includes unit tests for the abilities, weapons, and heroes. You can run these tests using `pytest`. Make sure you have it installed first:

```bash
pip install pytest
```

Then, run the tests by executing:

```bash
pytest hero_test.py
```

## Acknowledgments
- Inspired by classic RPG mechanics and simulation games.
- Thanks to the Python community for ongoing support and resources.

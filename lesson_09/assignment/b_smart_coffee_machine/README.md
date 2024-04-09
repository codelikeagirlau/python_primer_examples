# Smart Coffee Machine Project

## Overview

This project simulates a smart coffee machine using object-oriented programming principles in Python. It features a parent class `KitchenAppliance` and a subclass `SmartCoffeeMachine` that inherits from it. Users can add custom coffee types to the machine's menu and request the machine to make a coffee. If the requested coffee type is on the menu, the machine will proceed; otherwise, it will notify the user that the item is not available and display the current menu.

## Structure

The project is organized as follows:

- `kitchen_appliances/`
  - Contains the source code for the project.
  - `kitchen_appliance.py`: Defines the `KitchenAppliance` class.
  - `smart_coffee_machine.py`: Defines the `SmartCoffeeMachine` class.
- `scripts/`
  - Contains executable scripts, at the moment just `main.py`, which runs the coffee machine simulation.

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-coffee-machine.git
   cd smart-coffee-machine
   ```

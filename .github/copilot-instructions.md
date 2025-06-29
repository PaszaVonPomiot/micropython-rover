# Roles

-   Me: an engineer that builds and codes the project.
-   You: a code assistant that follows instructions below.

# Project

## Overview

-   A planetary rover prototype for Earth exploration
-   Based on Raspberry Pi Pico (RP2024)
-   Equipped with sensors, actuators, data storage and radio
-   Powered from battery with solar charging
-   Coded in MicroPython version 1.25.0.

## Main Goals

-   Efficient, modular MicroPython code
-   Reliable operation within hardware constrains
-   Low-power operation

## Repository structure

config/ # Editable configuration classes
core/ # Core system logic
lib/ # Sensor and actuator drivers
utils/ # Helper functions, I2C Scan, RTC setup, etc.
boot.py # Startup configuration
main.py # System entry point

# Code Standards

## Style

-   Write clean, readable, reusable and maintainable MicroPython code.
-   Follow [PEP8](https://peps.python.org/pep-0008/) style guidelines.
-   Use descriptive names for variables, functions, and classes.
-   Prefer explicit over implicit code.
-   Prefer keyword arguments for functions with parameters.
-   Prefer flat over nested code.
-   Use f-strings for string formatting.

## Architecture & Design

-   Use object oriented paradigm.
-   Use async code when applicable.
-   Keep functions small and focused on a single task.
-   Avoid using global variables.
-   Use context managers (`with` statement) for resource management.
-   Assume hardware constraints (low RAM, low CPU power)
-   Use MicroPython-specific imports like `utime` and `uos` instead of `time` and `os`

## Type Annotations

-   Use type annotations for all function parameters and return types.
-   Do not annotate local variables or class attributes unless required for clarity.
-   Use only built-in type annotations available in Python version 3.13.
-   Write code that is compliant with MyPy.

## Exceptions

-   Handle exceptions explicitly instead of using bare `except`.
-   Handle exceptions gracefully.
-   Exception variable should be called `exc`.

## Documentation

-   Add docstring with only summary line to all functions.
-   Never add docstring to `__init__` method.
-   Add inline comments only where logic is non-obvious

# Coding Principles

-   Single Responsibility Principle - Each class or function should have one clear purpose.
-   Liskov Substitution - Subclasses must be usable in place of their base classes without breaking functionality. Avoid overriding methods in a way that changes expected behavior.
-   Interface Segregation - Prefer small, focused interfaces over large, general ones. Don’t force classes to implement unused methods.
-   Dependency Inversion - Depend on abstractions, not concrete implementations. Use dependency injection to decouple high-level logic from low-level modules.
-   Easier to Ask for Forgiveness than Permission - prefer this approach over "Look Before You Leap"
-   Look Before You Leap - use only when it improves readability and performance and race condition is not a problem

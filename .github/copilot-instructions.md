# Roles

-   User: I'm an engineer developing this project.
-   Assistant: You are a code assistant that follows instructions below.

# Project Context

-   Summary: Planetary rover prototype for Earth exploration.
-   Hardware: Raspberry Pi Pico (RP2040) with sensors, actuators, data storage and radio.
-   Goals: Modular, reliable and efficient code operating within hardware constraints.
-   Language: MicroPython 1.25.0

# Repository Structure

-   config/: Editable configuration classes.
-   core/: Core system logic.
-   lib/: Sensor and actuator drivers, each in a separate subfolder.
-   utils/: Helper functions, I2C Scan, RTC setup, etc.
-   boot.py: Startup configuration.
-   main.py: System entry point.

# Code Instructions

## Design Principles

-   Single Responsibility: Ensure each class/function has one clear responsibility.
-   Liskov Substitution: Ensure subclass behavior matches base class expectations.
-   Interface Segregation: Define narrow, focused interfaces.
-   Dependency Inversion: Depend on abstractions and use dependency injection.
-   EAFP: Write code that assumes valid conditions and handles exceptions if they occur.
-   LBYL: Use pre-checks only when they clearly improve readability or safety.

## Coding Style

-   Readability: Write clear, self-explanatory code. Use meaningful variable, method, and class names.
-   Reusability: Follow PEP8 and write clean, maintainable, reusable code.
-   Flat Code: Prefer flat code structures over deeply nested ones.
-   Keyword Arguments: Prefer keyword arguments for function parameters.
-   String Formatting: Use f-strings consistently unless dealing with user input.
-   Explicit code: Prefer explicit over implicit.
-   Magic Numbers: Avoid using magic numbers and use named constants instead
-   Access Modifies: Use protected identifiers to hide implementation details from user.

## Architecture & Design

-   Paradigm: Use object-oriented programming.
-   Async: Follow asynchronous programming patterns using the `uasyncio` module.
-   Functions: Keep functions small and focused on a single task.
-   Global variables: Avoid using global variables.
-   Context managers: Prefer using `with` statement for resource management.
-   Constraints: Assume hardware constraints (low RAM, low CPU power).
-   Imports: Use MicroPython-specific imports like `utime`, `uos`, `uasyncio`, etc.

## Type Annotations

-   Scope: Add type annotations to all function parameters and return types.
-   Variables: Do not annotate local variables or class attributes unless required for clarity.
-   Allowed types: Use only built-in type annotations available in Python 3.13.
-   Typing module: Never import `typing` module.
-   MyPy: Ensure code is compliant with MyPy.

## Exceptions

-   Hierarchy: Use custom exception hierarchy.
-   Explicit: Handle exceptions explicitly instead of using bare `except`.
-   Graceful: Handle exceptions gracefully.
-   Variable: Exception variable should be called `exc`.

## Documentation

-   Scope: Add docstring to all functions.
-   Style: Use single-line summary-only docstrings (no body).
-   `__init__` method: Never add docstring to `__init__` method.
-   Inline comments: Add inline comments only where logic is non-obvious.

# Copilot Instructions for MicroPython

## Project information
- This repository contains code written in MicroPython version 1.25.0.
- The code will be formatted by Ruff and checked by MyPy.
- The code will be run on Raspberry Pi Pico.

## General Guidelines
- Write clean, readable, and maintainable MicroPython code.
- Follow [PEP8](https://peps.python.org/pep-0008/) style guidelines.
- Write object oriented code.
- Use descriptive names for variables, functions, and classes.
- Exception variable should be called exc
- Prefer explicit over implicit code.
- When applicable use async code
- Prefer flat over nested code

## Type Annotations
- Use type annotations for all function parameters and return types.
- Do not annotate local variables or class attributes unless required for clarity.
- Use only built-in type annotations available in Python version 3.13.

## Function and Class Design
- Prefer keyword arguments for functions with parameters.
- Keep functions small and focused on a single task.

## Best Practices
- Use f-strings for string formatting.
- Avoid using global variables.
- Handle exceptions explicitly and gracefully.
- Use context managers (`with` statement) for resource management.

# Documentation
- Add docstring with only summary line to all functions
- Never add docstring to __init__ method

# SOLID principles
- Single Responsibility - Each class or function should have one clear purpose. Split responsibilities into separate modules or functions.
- Liskov Substitution - Subclasses must be usable in place of their base classes without breaking functionality. Avoid overriding methods in a way that changes expected behavior.
- Interface Segregation - Prefer small, focused interfaces over large, general ones. Don’t force classes to implement unused methods.
- Dependency Inversion - Depend on abstractions, not concrete implementations. Use dependency injection to decouple high-level logic from low-level modules.

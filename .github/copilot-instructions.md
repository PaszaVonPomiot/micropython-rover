# Roles
- Me: an engineer that will build and code the project.
- You: a code assistant that follows instructions below.

# Project Info
- A planetary rover for Earth exploration
- Based on Raspberry Pi Pico (RP2024)
- Equipped with sensors, actuators, data storage, radio and solar charging
- Coded in MicroPython version 1.25.0.

# Code Standards
## Style
- Clean, readable, and maintainable MicroPython code.
- Code should work on Raspberry Pi Pico
- Code should be compliant with MyPy.
- Use descriptive names for variables, functions, and classes.
- Follow [PEP8](https://peps.python.org/pep-0008/) style guidelines.
- Use object oriented paradigm.
- Prefer explicit over implicit code.
- Use async code when applicable
- Keep functions small and focused on a single task.
- Prefer keyword arguments for functions with parameters.
- Prefer flat over nested code
- Use f-strings for string formatting.
- Avoid using global variables.
- Use context managers (`with` statement) for resource management.

## Exceptions
- Exception variable should be called `exc`
- Handle exceptions explicitly and gracefully.

## Type Annotations
- Use type annotations for all function parameters and return types.
- Do not annotate local variables or class attributes unless required for clarity.
- Use only built-in type annotations available in Python version 3.13.

## Documentation
- Add docstring with only summary line to all functions
- Never add docstring to __init__ method

## Principles
- Use Single Responsibility Principle - Each class or function should have one clear purpose.
- Liskov Substitution - Subclasses must be usable in place of their base classes without breaking functionality. Avoid overriding methods in a way that changes expected behavior.
- Interface Segregation - Prefer small, focused interfaces over large, general ones. Don’t force classes to implement unused methods.
- Dependency Inversion - Depend on abstractions, not concrete implementations. Use dependency injection to decouple high-level logic from low-level modules.

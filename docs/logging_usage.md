# Logging Usage Guide

The Python logging module provides a way to track events that happen when some software runs. The log records can provide critical information when diagnosing problems, understanding software behavior, and auditing actions.

## Logger Configuration

Our logger is configured in `logger.py`. It logs messages to both the console and a file named `app.log` located in the `logs` directory. The logger captures all log levels by default.

## Log Levels

The logger supports several levels of severity. The standard levels and their applicability are as follows:

- **DEBUG**: Detailed information, typically of interest only when diagnosing problems.
- **INFO**: Confirmation that things are working as expected.
- **WARNING**: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., 'disk space low'). The software is still working as expected.
- **ERROR**: Due to a more serious problem, the software has not been able to perform some function.
- **CRITICAL**: A serious error, indicating that the program itself may be unable to continue running.

## Usage

To use the logger, first import it in your Python script:

```python
from logger import logger
```

Then, you can log messages like this:

```python
logger.info("This is an informational message")
logger.error("This is an error message")
```

## Choosing the Right Log Level

- Use **DEBUG** for detailed diagnostic information. Use it when you're developing or diagnosing an issue.
- Use **INFO** for general operational messages that confirm the program is working as expected.
- Use **WARNING** when something unexpected happens, but the program is still working as expected.
- Use **ERROR** when the program encounters a problem that prevents it from doing something.
- Use **CRITICAL** when there's a severe problem that might cause the program to stop running entirely.

Remember, effective logging is crucial for understanding and debugging the behavior of applications, especially in production environments. Choose the log level wisely to ensure the logs are informative and not too verbose.

This guide and the associated logger configuration provide a solid foundation for logging in Python projects. You can further customize the logger and the documentation to fit the specific needs of your project or organization.

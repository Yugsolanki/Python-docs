---
title: Argument Passing
sidebar_position: 1
---

# Argument Passing in Python

In Python, when you run a script or command from the terminal, you can pass arguments along with it. These arguments, along with the script name itself, are stored in a list called `argv` in the `sys` module.

Here's how it works:

1. When you run a script, Python collects the script name and any additional arguments you provide.
   
2. These are then stored as strings in the `sys.argv` list.
   
3. The length of `sys.argv` is always at least one. If no script name or arguments are provided, `sys.argv[0]` is an empty string.

4. If the script is read from standard input (`-`), `sys.argv[0]` is set to `-`.
   
5. If you're using the `-c` option to run a command, `sys.argv[0]` is set to `-c`.
   
6. If you're running a module using the `-m` option, `sys.argv[0]` is set to the full name of the located module.
   
7. Any options found after `-c` or `-m` are not processed by Python's option handling and are left in `sys.argv` for the command or module to handle.

To access these arguments in your Python script, you need to import the `sys` module and then use `sys.argv`.

For example:

```python
import sys

script_name = sys.argv[0]
arguments = sys.argv[1:]

print("Script Name:", script_name)
print("Arguments:", arguments)
```

This allows you to pass information to your Python scripts from the command line, making them more versatile and adaptable to different scenarios.
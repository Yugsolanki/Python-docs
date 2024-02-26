---
title: Source Code Encoding
sidebar_position: 1
---

# Source Code Encoding in Python

By default, Python assumes that source code files are encoded in UTF-8, which supports characters from most languages worldwide. This means you can use characters from various languages in string literals, identifiers, and comments. However, the standard library only uses ASCII characters for identifiers, so it's best practice to follow this convention for portable code.

If you need to use a different encoding for your source code files, you can declare it using a special comment line at the beginning of the file. The syntax for this comment line is:

```python
# -*- coding: encoding -*-
```

Here, `encoding` should be replaced with the name of the desired encoding, which must be one of the valid codecs supported by Python.

For example, if you want to use the Windows-1252 encoding, you should add the following line as the first line of your source code file:

```python
# -*- coding: cp1252 -*-
```

One exception to this rule is when the source code starts with a UNIX "shebang" line. In this case, the encoding declaration should be added as the second line of the file, following the shebang line.

For example:

```python
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```

Ensure that your text editor recognizes the chosen encoding and uses a font that supports all the characters in the file to display them properly.

This encoding declaration helps Python interpret the source code correctly, especially when dealing with non-ASCII characters or specific character encodings. It's a good practice to include this declaration in your source code files to avoid any potential issues with character encoding.
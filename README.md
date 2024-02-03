# Beautifish: Shell Data Decorator & Icons Library

`beautifish` is a Python package that provides a set of utilities for decorating and enhancing the visual representation of data in the shell, along with a collection of shell icons to make your terminal experience more delightful.

```bash
pip install beautifish
```

## :sparkles: Features

- **Shell Data Decoration:** Beautify your shell output by using decorators to highlight and structure data.
- **Shell Icons Library:** A collection of icons to use in your shell scripts or outputs.

## :arrow_down: Installation

You can install `beautifish` using `pip`:

```bash
pip install beautifish
```


## :desktop: Usage

### Shell data decoration

Initialize beautifish client and turn desired texts into colored shell texts:

```bash
from beautifish import initialize as beautifish_init
beautifish = beautifish_init.beautifish_initalize()
```

```bash
s = "Beautiful fishes"
s = beautifish.blue_text(s)
s = beautifish.green_text(s)
```

### Shell icons library

Import and use all supported shell icons out-of-the-box:

```bash
from beautifish.shell_icons import *

msg = f"{TICK} Correct answer"
err = f"{CROSS} Wrong answer"
```

Supported shell icons:

`TICK`, `CROSS`, `DOT` 



## :handshake: Contributions

Contributions are welcome! 

If you have ideas for improvements, new features, or bug fixes, please feel free to open an issue or submit a pull request.



## :book: License

This project is licensed under the MIT License - see the <a href=''>LICENSE</a> file for details.

<hr>

© 2024 dev-kushalkumar

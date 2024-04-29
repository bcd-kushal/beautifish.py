# Beautifish: Console Decorator & Icons Library

<img style="width:24px" title="python3" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png"/> &nbsp;
<img style="width:24px" title="linux" src="https://github.com/marwin1991/profile-technology-icons/assets/76662862/2481dc48-be6b-4ebb-9e8c-3b957efe69fa"/> &nbsp;
<img style="width:24px" title="windows" src="https://user-images.githubusercontent.com/25181517/186884150-05e9ff6d-340e-4802-9533-2c3f02363ee3.png"/> &nbsp;
<img style="width:24px" title="macOS" src="https://user-images.githubusercontent.com/25181517/186884152-ae609cca-8cf1-4175-8d60-1ce1fa078ca2.png"/> &nbsp;
<img style="width:24px" title="jupyter" src="https://user-images.githubusercontent.com/25181517/183914128-3fc88b4a-4ac1-40e6-9443-9a30182379b7.png"/> &nbsp;

`beautifish` is a Python package that provides a set of utilities for decorating and enhancing the visual representation of data in the console, along with a collection of supported icons to make your console experience more delightful.

```bash
pip install beautifish
```

## :sparkles: Features

- **Console Data Decoration:** Beautify your console output by using decorators to highlight, format and structure data.
- **Pre-defined Templates:** A collection of important templates to get started with, to put aside the worry of its UI.
- **Supported Icons Library:** A collection of icons to use in your console scripts or outputs.

A complete documentation will be out soon for the same.

## :arrow_down: Installation

You can install `beautifish` using `pip`:

```bash
pip install beautifish
```

## :sunflower: Usage

### Console data decoration

Initialize beautifish client and turn desired texts into colored shell texts:

```python
import beautifish.decorators as bfd
import beautifish.colors as bfc
```

```python
# beautifish.decorators as bfd
s = "Beautiful fishes"
s = bfd.italic(s)
s = bfd.strikethrough(s)

# beautifish.colors as bfc
s = "Beautiful fishes"
s = bfc.blue_text(s)     
s = bfc.green_text(s)
```

### Pre-defined templates

Import and use from a plethora of useful templates for productivity and focusing on the work at hand:

```python
import beautifish.templates as bft
```

```python
# show data as tree
data = {...}  
bft.tree(data)

# color your inputs  
age = bft.input("Enter age:")

# create loading bar
bft.loading_bar(iterations=40,msg="Downloading")

# create ascii text banner
bft.banner("Beautifish",color="yellow")
```

### Supported icons library

Import and use all supported shell icons out-of-the-box:

```python
import beautifish.icons as bfi

msg = f"{bfi.TICK} Correct answer"
err = f"{bfi.WARNING} Sure to proceed?"
```

All supported icons:

`TICK`, `CROSS`, `DOT`, `WARNING`, `ARROW_DOWN`, `ARROW_UP`, `ARROW_LEFT`, `ARROW_RIGHT`, `ARROW_RIGHT2`, `SPARKLE`, `STAR`, `CLOCK`, `DANGER`,  `DASH`, `CHECK`, `LIGHTNING`, `HOURGLASS`  

<hr>


## :handshake: Contributions

Contributions are welcome! 

If you have ideas for improvements, new features, or bug fixes, please feel free to open an issue or submit a pull request.


## ⚖️ License

This project is licensed under the MIT License - see the <a href=''>LICENSE</a> file for details.

<hr>

<h3><img title="Kushal-Kumar" width="18" src="https://raw.githubusercontent.com/bcd-kushal/bcd-kushal/main/assets/icons/dark/filled/kushalkumar_bg_dark.png"/>&nbsp;Kushal Kumar 2024 • All rights reserved </h3>

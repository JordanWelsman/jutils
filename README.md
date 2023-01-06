```ascii
    _       _   _ _     
   (_)_   _| |_(_) |___ 
   | | | | | __| | / __|
   | | |_| | |_| | \__ \
  _/ |\__,_|\__|_|_|___/
 |__/                                                     
```

A Python package of useful tools and utilities.

# Overview

`jutils` is a simple `Python 3.10+` package which gives the user various tools. These tools are broken down into sub-modules in which the user can import individually.

# Table of contents

- [Overview](#overview)
- [Table of contents](#table-of-contents)
- [Install \& use](#install--use)
  - [Test](#test)
  - [Build](#build)
- [Objectives](#objectives)
- [History](#history)
  - [`0.0.0` (12.30.2022)](#000-12302022)
  - [`0.0.1` (01.06.2023)](#001-01062023)
- [Credits](#credits)
- [Licence](#licence)
- [Links](#links)

# Install & use

1. From terminal: `pip install juts`
2. From python environment: `from jutils import <submodule>` where `<submodule>` is:

- `averages`
- `calculators`
- `converters`
- `cryptography`
- `formatting`
- `language`
- `logic`
- `pipelining`
- `sorters`
- `timers`
- `utilities`

## Test

1. Clone repository: `git clone https://github.com/JordanWelsman/jutils.git`
2. Build module for testing: `python3 setup.py bdist_wheel`
3. Install module locally: `pip install jutils -e . dev`
4. Run tests with PyTest: `pytest`

## Build

1. Build module for distribution: `python3 setup.py bdist_wheel sdist`
2. Push to PyPI: `pip install twine` `twine upload dist/*`

# Objectives

- Publish a package of tools I have developed that I use in production applications.
- Help other users improve their workflows and contribute to more performant applications.

# History

## `0.0.0` (12.30.2022)

- GitHub reposotiry created
- Project created
	- Basic readme created

## `0.0.1` (01.06.2023)

- Project uploaded to PyPI
- Ability to unbuild project
    - Unbuild script (`./unbuild`)
- Hello, World! function

# Credits

`jutils` was created, developed, and is currently maintained by **Jordan Welsman**.

# Licence

`jutils` is developed and distributed under the `MIT` license.
> See `LICENSE` for more details.

# Links

:file_folder: [See this project on GitHub](https://github.com/JordanWelsman/jutils/)

:gift: [See this project on PyPI](https://pypi.org/project/jutl/)

:cat: [Follow me on GitHub](https://github.com/JordanWelsman/)

:briefcase: [Connect with me on Linkedin](https://linkedin.com/in/JordanWelsman/)

:email: [Send me an email](mailto:jordan.welsman@outlook.com)

:clapper: [Followed tutorial](https://www.youtube.com/watch?v=GIF3LaRqgXo/) by [Mark Smith (@judy2k)](https://twitter.com/judy2k/)

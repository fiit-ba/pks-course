# The validator for PKS network analyzer



## Getting started

Simple tool for validation of the correct YAML syntax output from the network analyzer.

## Prerequisites

LINUX:

- python 3.6+ and python3-pip
```
apt install python3 python3-pip
```
- argparse, PyYaml and Yamale
```
pip install argparse pyyaml yamale ruamel.yaml
```

Windows:

https://www.digitalocean.com/community/tutorials/install-python-windows-10

## Usage
You can get help.
```
python3 validator.py -h
```

You can use default schema and output.
```
python3 validator.py
```

You can specify the schema using the command option -s/--schema.
```
python3 validator.py -s ./schemas/schema.yaml
```

You can specify the yaml output using the command -d/--data.
```
python3 validator.py -d ./examples/packets-all.yaml
```

## Authors
[Lukas Mastilak](https://gitlab.com/luka73), STU FIIT

## Acknowledgment
[Kristian Kostal](https://scholar.google.sk/citations?user=6b4HfA4AAAAJ&hl=sk), STU FIIT

[Pavol Helebrandt](https://scholar.google.sk/citations?user=xdloWxEAAAAJ&hl=en), STU FIIT

## License
Distributed under the MIT License. See `LICENSE` for more information.

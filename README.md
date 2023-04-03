# Grepper Python Client
The Grepper Python library provides convenient access to the Grepper API from applications written in the Python language.

## Requirements
Python 3.7 and later.

## PIP
Coming soon.

## Manual Installation
```bash
git clone https://github.com/CantCode023/grepper-python
cd grepper-python
python setup.py install
```

## Getting Started
Simple usage:
```py
grepper = Grepper("your-grepper-api-key")
answers = grepper.search("query")
print(answers)
```
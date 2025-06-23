## Problem Set 4
This project includes implementations of the RSA algorithm and a simulation of an attack on an encrypted message.

These problems were developed and tested as part of Discrete Mathematics course.


## Installation
Make sure you have Python 3.10+ installed. Then, clone the repository and install the project in editable mode with:

```bash 
pip install -e .
```

This allows you to make changes in the source code without reinstalling the package.


## Requirements
To install the packages, you can run:
```bash
pip install -r requirements.txt
```


## Usage
To run the test scenarios :

```bash
python tests/test_basic_rsa.py
```
Runs tests to verify whether the RSA encryption and decryption algorithms work correctly, and whether an attack on small keys is effective

```bash
python tests/test_timing.py
```
Runs tests to measure how long it takes to break a key depending on its size.


## Author
This project was developed as part of the second problem set in a Discrete Mathematics course by Louis Bonnecaze (Louis641214).
# Password Generator


## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the code](#running-the-code)
- [License](#license)



## Introduction
The following software is my version of the final work of the course ["Definitive Programming Course with Python"](https://kazel.academy/cursos/python) given by Facundo Garcia Martoni, CEO and professor at Kazel Academy.

## Getting Started
This is a Python script that generates a secure and random password for the user. It allows the user to specify the desired length of the password and whether or not they want to include uppercase and lowercase letters, digits, and symbols. 

The script use the **secrets** module is a Python library that provides functions for generating cryptographically secure random numbers, bytes, and sequences. It is similar to the **random** module, but is specifically designed for generating secure random numbers that can be used for cryptographic purposes.

The main difference between **random** and **secrets** is that secrets uses cryptographic entropy sources to generate random numbers, while random uses more predictable and less secure entropy sources. The module **secrets** is designed for the generation of cryptographic keys, passwords and other sensitive data that requires high entropy.

## Prerequisites
To run this game, you need to have Python 3 installed on your system.
- Python version 3.6 or newer 
- **string** **secrets**, and **getpass** modules, which are included in the standard Python library.

## Installation
Clone this repository to your local machine using:
```sh
git clone https://github.com/horacio-gaido/password_generator.git
```

## Running the code
To run the software, open a terminal or command prompt and navigate to the directory where you cloned the repository. Then, enter the following command:
```sh
py password_generator.py
```

The script first prompts the user to answer a series of questions using the ask_question() function to determine which types of characters to include in the password.

It then declares the possible characters of the password using the string.printable attribute, which includes all printable ASCII characters except whitespace and quotes.

The script generates a random password by first including at least one lowercase letter and then adding uppercase letters, digits, and symbols if the user requested them. It then fills the remaining characters with random characters from the possible characters list.

Finally, the password is shuffled using the secrets.SystemRandom().shuffle() method to ensure it is truly random and difficult to guess. The generated password is displayed on the screen using the print() function.

## License

This investigation is licensed under the MIT License. See the [LICENSE.md](https://github.com/horacio-gaido/password_generator/blob/main/LICENCE.md) file for details.
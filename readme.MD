# An Introduction to Flask-SQLAlchemy in Python
This code reports the whole code of the article [An Introduction to Flask-SQLAlchemy in Python](https://blog.appsignal.com/2025/02/26/an-introduction-to-flask-sqlalchemy-in-python.html)

## Prerequisites
To replicate the example reported in the article, your system must satisfy the following prerequisites:

- [Ubuntu](https://ubuntu.com/) (any recent version) for [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install): The steps in this tutorial are tailored for Ubuntu in WSL, but they are adaptable to other Linux distributions, especially not under WLS, or for different Operating Systems (but you'll need to adapt the code).
- [Python 3.6+](https://www.python.org/downloads/): Flask-SQLAlchemy requires Python 3.6 or higher. 
- [MySQL](https://www.mysql.com/): The steps in this guide are tested with MySQL installed (on Ubuntu for WSL).
- Basic knowledge of [Python](https://www.python.org) and [Flask](https://flask.palletsprojects.com/en/stable/): This tutorial requires familiarity with virtual environments, Flask application structure, and basic terminal commands.

## Overview of The Article
The article presents [SQLAlchemy](https://www.sqlalchemy.org/) as a powerful tool to manage databases using Python.

Specifically, using [Flask-SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/en/stable/) makes it easier to manage databases as this extension leverages SQLAlchemy specifically for Flask apps.

The example you can run through in the article shows how easy it is to use this library.
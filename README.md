# Profile System

This script creates a web application using FastAPI to manage a user database. It provides routes for displaying the
main page, user list, user profile, adding users, and deleting users. It also uses Jinja2Templates for rendering HTML
templates and SQLAlchemy for interacting with the database.

![Python](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058) ![fastapi](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)

## Features

- Provides routes for displaying the main page, user list, user profile, adding users, and deleting users
- Uses Jinja2Templates for rendering HTML templates to create dynamic content in the user interface
- Utilizes SQLAlchemy for database operations such as querying users and committing changes

## Example

To start local server, run the script:

```sh
python main.py
```

## Motivation

The motivation for this project is to create a web application that allows users to interact with a user database
through a user-friendly interface. By using FastAPI, Jinja2Templates, and SQLAlchemy, the project aims to provide a
seamless experience for users to view, add, and delete user information. The inclusion of error handling with
appropriate error messages enhances the project's usability and reliability.

## Requirements

- Python 3.8+
- fastapi 0.111.0
- SQLAlchemy 2.0.31

## Installation and Usage

1. Clone the repository or download the script.
2. Install the required packages:

```sh
pip install requirements.txt
```

3. Run the script:

```sh
python main.py
```

## Contributors

To contribute to this project, you can create an issue or submit a pull request.

## Reference

- [Python Official Documentation](https://docs.python.org/3/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)

## License

- [MIT License](https://opensource.org/license/mit)
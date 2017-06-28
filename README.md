# ToDo List API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains a fully working API project which serves as an interface for interacting with a ToDo List Application.

## Development
This application was developed using [Flask](http://flask.pocoo.org/). Postgres was used for persisting data with [SQLAlchemy](https://www.sqlalchemy.org/) as [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping).

## Installation
* Start up your terminal (or Command Prompt on Windows OS).
* Ensure that you've `python` installed on your PC.
* Clone the repository by entering the command `git clone https://github.com/andela-bolajide/ToDoListAPI` in the terminal.
* Navigate to the project folder using `cd ToDoListAPI` on your terminal (or command prompt).
* After cloning, create a virtual environment then install the requirements with the command:
`pip install -r requirements.txt`.
* After this, you'll need initialize a PostgreSQL database using the command: `python manage.py db init`
* Then to migrate data schema to the database using the command: `python manage.py db migrate` then `python manage.py db upgrade`.

## Usage
* A customized interactive python shell can be accessed by passing the command `python manage.py shell` on your terminal.
* Once this is done, the application can be started using `python manage.py runserver` and by default the application can be accessed at `http://127.0.0.1:5000`.

## API Documentation
-----
The API has routes, each dedicated to a single task that uses HTTP response codes to indicate API status and errors.

#### API Features

The following features make up the ToDoList API:

###### ToDoList

-   It allows new ToDoLists to be created by users.

-   It allows the users to create, retrieve, modify, and delete ToDoLists.



| EndPoint                                 | Functionality                 | Public Access |
| -----------------------------------------|:-----------------------------:|--------------:|
| **POST** /todolists/                     | Create a new To Do List       |    TRUE       |
| **GET** /todolists/                      | List all created todolists    |    TRUE       |
| **GET** /todolist/id                     | Get single todo list          |    TRUE       |
| **PUT** /todolist/id                     | Update a todo list            |    TRUE       |
| **DELETE** /todolist/id                  | Delete a ToDo List            |    TRUE       |

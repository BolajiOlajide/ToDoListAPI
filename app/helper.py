"""Define helper functions to be used here."""


def to_json(todolist):
    """Convert SQL queries to actual dictionaries."""
    result = {
        "id": todolist.todoList_id,
        "name": todolist.name,
        "date_created": todolist.date_created
    }
    return result

"""
This script contains the routes for the different API methods.

This handles the overall routing of the application.
"""
from flask import Blueprint, jsonify, request

from app.models import ToDoList
from app.helper import to_json

api = Blueprint('api', __name__)


@api.route('/todolists/', methods=['POST'])
def create_todolist():
    """
    Create a new ToDoList.

    Add a new todolist and returns the todolist for the user to view
    """
    todolist = ToDoList(name=request.json['name'],)
    todolist.save()
    return jsonify({
        "message": "{} has been added to your ToDo List."
                   .format(request.json['name']),
        "status": 201
    }), 201


@api.route('/todolists/', methods=['GET'])
def get_todolists():
    """
    Get all the created ToDo Lists.

    Displays a json of all the created ToDo List .
    """
    todolists = ToDoList.query.all()
    todo = [to_json(todolist) for todolist in todolists]
    return jsonify({
        "ToDo Lists": todo,
        "status": 200
    }), 200


@api.route('/todolists/<int:todolist_id>', methods=['GET'])
def get_todolist(todolist_id):
    """Get a particular todolist with it's ID."""
    todolist = ToDoList.query.filter_by(todoList_id=todolist_id).first()
    return jsonify({
        "ToDo List": to_json(todolist),
        "status": 200
    }), 200


@api.route('/todolists/<int:todolist_id>', methods=['DELETE'])
def delete_todolist(todolist_id):
    """Get a particular todolist with it's ID and delete it."""
    todolist = ToDoList.query.filter_by(todoList_id=todolist_id).first()
    todolist.delete()
    return jsonify({
        "message": "The todolist {} has been deleted.".format(todolist.name),
        "status": 200
    }), 200


@api.route('/todolists/<int:todolist_id>', methods=['PUT'])
def update_todolist(todolist_id):
    """Get a particular todolist with it's ID and update it."""
    todolist = ToDoList.query.filter_by(todoList_id=todolist_id).first()
    name = request.json.get('name', todolist.name)
    todolist.name = name
    todolist.save()
    return jsonify({
        "message": "The todolist {} has been updated.".format(todolist.name),
        "status": 200
    }), 200

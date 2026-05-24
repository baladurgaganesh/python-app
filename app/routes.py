# app/routes.py
from flask import Blueprint, jsonify, request
from app.models import Task

api = Blueprint('api', __name__)

@api.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(Task.list()), 200

@api.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing title"}), 400
    task = Task.create(data["title"])
    return jsonify(task), 201

@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    done = data.get("done")
    task = Task.update(task_id, done)
    if task:
        return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.delete(task_id)
    if task:
        return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

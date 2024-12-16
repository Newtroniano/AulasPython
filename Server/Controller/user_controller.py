from flask import request, jsonify
from Models.user_model import create_user, get_user, update_user, delete_user

def create_user_route():
    data = request.get_json()

    print(data)
    user_id = data.get("user_id")
    name = data.get("name")
    email = data.get("email")
    create_user(user_id, name, email)
    return jsonify({"message": "User created successfully"}), 201

def get_user_route(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

def update_user_route(user_id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    if update_user(user_id, name, email):
        return jsonify({"message": "User updated successfully"})
    return jsonify({"message": "User not found"}), 404

def delete_user_route(user_id):
    if delete_user(user_id):
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"message": "User not found"}), 404

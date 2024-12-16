from flask import Blueprint, request, jsonify
from Models.user_model import get_all_users, add_user, get_all_user

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/', methods=['GET'])
def index():
    users = get_all_users()  
    return jsonify(users)  


@user_bp.route('/<int:user_id>', methods=['GET'])
def getuser(user_id):
    users = get_all_user(user_id)  
    return jsonify(users)  

@user_bp.route('/add', methods=['POST'])
def add():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Missing data"}), 400

    add_user(username, email, password)  
    return jsonify({"message": "User added successfully"}), 201



# def create_user_route():
#     data = request.get_json()

#     print(data)
#     user_id = data.get("user_id")
#     name = data.get("name")
#     email = data.get("email")
#     create_user(user_id, name, email)
#     return jsonify({"message": "User created successfully"}), 201

# def get_user_route(user_id):
#     user = get_user(user_id)
#     if user:
#         return jsonify(user)
#     return jsonify({"message": "User not found"}), 404

# def update_user_route(user_id):
#     data = request.get_json()
#     name = data.get("name")
#     email = data.get("email")
#     if update_user(user_id, name, email):
#         return jsonify({"message": "User updated successfully"})
#     return jsonify({"message": "User not found"}), 404

# def delete_user_route(user_id):
#     if delete_user(user_id):
#         return jsonify({"message": "User deleted successfully"})
#     return jsonify({"message": "User not found"}), 404

from flask import Flask
from Controller.user_controller import create_user_route, get_user_route, update_user_route, delete_user_route

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def create_user():
    return create_user_route()

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return get_user_route(user_id)

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return update_user_route(user_id)

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return delete_user_route(user_id)

if __name__ == '__main__':
    app.run(debug=True)

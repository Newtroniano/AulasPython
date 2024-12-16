from flask import Flask
from Controller.user_controller import user_bp
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  
app.config['MYSQL_PASSWORD'] = 'luis123'  
app.config['MYSQL_DB'] = 'game_db'

mysql = MySQL(app)
app.register_blueprint(user_bp)

# @app.route('/user', methods=['POST'])
# def create_user():
#     return create_user_route()

# @app.route('/user/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     return get_user_route(user_id)

# @app.route('/user/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     return update_user_route(user_id)

# @app.route('/user/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     return delete_user_route(user_id)

if __name__ == '__main__':
    app.run(debug=True)

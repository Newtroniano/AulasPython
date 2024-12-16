from flask_mysqldb import MySQL

mysql = MySQL()

def get_all_users():
    """Retorna todos os usuários do banco de dados."""
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    users = cur.fetchall()
    cur.close()
    return users

def get_all_user(id):
    """Retorna todos os usuários do banco de dados."""
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM user WHERE user.id = %s', (id,))
    users = cur.fetchall()
    cur.close()
    return users


    print("aquiiiiiii", users)
    return users

def add_user(username, email, password):
    """Adiciona um novo usuário ao banco de dados."""
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    mysql.connection.commit()
    cur.close()

# users_db = {}

# def create_user(user_id, name, email):
#     users_db[user_id] = {"name": name, "email": email}

# def get_user(user_id):
#     return users_db.get(user_id, None)

# def update_user(user_id, name, email):
#     if user_id in users_db:
#         users_db[user_id] = {"name": name, "email": email}
#         return True
#     return False

# def delete_user(user_id):
#     if user_id in users_db:
#         del users_db[user_id]
#         return True
#     return False



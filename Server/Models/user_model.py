# Simulando uma base de dados com um dicionário
users_db = {}

def create_user(user_id, name, email):
    users_db[user_id] = {"name": name, "email": email}

def get_user(user_id):
    return users_db.get(user_id, None)

def update_user(user_id, name, email):
    if user_id in users_db:
        users_db[user_id] = {"name": name, "email": email}
        return True
    return False

def delete_user(user_id):
    if user_id in users_db:
        del users_db[user_id]
        return True
    return False

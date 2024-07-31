from user_session import User

def registration_new_user(id_user: str):
    path = f'.\\users\\{id_user}.json'
    user = User(id_user, path)
    return user
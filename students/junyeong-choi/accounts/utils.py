import jwt

from project_westagram.my_settings import SECRET_KEY, ALGORITHM

def encoded_jwt(account_id):
    token = jwt.encode({'account_id': account_id}, SECRET_KEY, ALGORITHM)
    return token
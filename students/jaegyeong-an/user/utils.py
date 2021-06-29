import jwt

from westagram.settings import SECRET_KEY

def encode_jwt(user_id):
    access_token = jwt.encode({'user_id':user_id}, SECRET_KEY, algorithm='HS256')
    return access_token
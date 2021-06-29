import jwt
import json

from my_settings import SECRET_KEY

def check_token(token):
    check_token = jwt.decode( token, SECRET_KEY, algorithms='HS256')
    return check_token


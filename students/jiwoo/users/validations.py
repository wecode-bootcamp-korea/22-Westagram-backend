import re ,bcrypt, jwt

from my_settings import SECRET_KEY

def password_check(password): 
    password_regex = re.compile('.{8,45}')
    return password_regex.match(password)

def create_bcrypt(password): 
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def check_bcrypt(password, hashed_password): 
    return bcrypt.checkpw(password.encode('utf-8'),hashed_password)


def create_jwt(num): 
    SECRET       = SECRET_KEY
    access_token = jwt.encode({'id' : num}, SECRET, algorithm = 'HS256')
    return access_token
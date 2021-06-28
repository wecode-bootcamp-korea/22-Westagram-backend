import re 

def password_check(password):
    password_regex = re.compile('.{8,45}')
    return password_regex.match(password)
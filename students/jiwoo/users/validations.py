import re 

def password_check(password):
    password_regex = re.compile('.{8,45}')
    return password_regex.match(password)

def email_check(email): 
    email_regex = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return email_regex.match(email)

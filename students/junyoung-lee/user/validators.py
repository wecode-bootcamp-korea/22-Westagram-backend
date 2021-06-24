import re

from django.core.exceptions import ValidationError

def validate_email(email): 
    email_regex = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not (re.search(email_regex, email)):
        


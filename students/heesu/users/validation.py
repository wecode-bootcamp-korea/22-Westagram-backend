import re

from django.core.exceptions import ValidationError

EXPRESSION = {
        "email" : '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        "phone_number" : "\d{3}-\d{3,4}-\d{4}"
    }

class expression() :
    def vaild_check(pattern_name,value) :
        pattern = EXPRESSION[pattern_name]
        pattern_test = re.compile(pattern).match(value)
        return bool(pattern_test)
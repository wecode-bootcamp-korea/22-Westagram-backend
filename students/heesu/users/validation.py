import re

from django.core.exceptions import ValidationError

EXPRESSION = {
        "email" : '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        "phone_number" : "\d{3}-\d{3,4}-\d{4}"
    }

class expression() :
    def vaild_check(input_data) :
        def expression(**kwargs):
            key = list(kwargs.keys())[0]
            value = list(kwargs.values())[0]
            pattern = EXPRESSION[key]
            pattern_test = re.compile(pattern).match(value)

            if not bool(pattern_test) :
                raise ValidationError(key + "_ERROR")
            
        for i in range(0,len(input_data)) :
            key = (list(input_data.keys())[i])
            value = (list(input_data.values())[i])

            if key == "phone_number" :
                expression(phone_number = value)

            if key == "email" :
                expression(email = value) 

            if key == "password" :    
                if len(input_data[key]) < 8 :
                    raise ValidationError("PASSWORD_ERROR")
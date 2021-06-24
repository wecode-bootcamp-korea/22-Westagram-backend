import json
from django import views
from django.http import JsonResponse
from django.views import View
from .models import USER, USERINFO

# Create your views here.
class USERVIEW(View) :
    def post(self, request) :
        data = json.loads(request.body)

        if(USER.objects.filter(name=data['owner']).exists()) :
            owner = Owner.objects.get(name=data['owner'])
            dog = Dog.objects.create(
            name=data['dog_name'],
            age=data['dog_age'],
            owner = owner
        )
        else :
            owner = Owner.objects.create(
                name = data['owner'],
                email = data["email"],
                age = data['age']
                )
            dog = Dog.objects.create(
                name=data['dog_name'],
                age=data['dog_age'],
                owner = owner
            )

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self, request) :
        
        Owners = Owner.objects.all()
        result = []
        for o in Owners :
            dogs = o.dog_set.all()
            dog_lst = []
            for d in dogs :
                dog_info = {
                    "name": d.name,
                    "age" : d.age

                } 
                dog_lst.append(dog_info)
            
            owner_info = {
                "email" : o.email,
                "name" : o.name,
                "age" : o.age,
                "dogs" : dog_lst
            }
            result.append(owner_info)   


        return JsonResponse({"results" : result}, status = 200)        
    
import json 

from django.http             import JsonResponse
from django.views            import View 

from postings.models         import Post
from users.models            import User


# Create your views here.
class CreatePostsView(View):
    def post(self, request):

        try: 
            data = json.loads(request.body)
            user = User.objects.get(name=data['name'])
            
            Post.objects.create(
                user=user,
                title = data['title'],
                content = data['content'],
                image_url = data['image_url']
            )
            
            return JsonResponse({"message":"SUCCESS"},status =201)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"},status=400)


    def get(self, request):

        results= [({"user" : user.name, "post" : [(post.title, post.content, post.created_at) for post in user.post_set.all()]}) for user in User.objects.all()]
        


        return JsonResponse({"results":results}, status = 200)



    # def get(self, request):
        
    #     for문 + list comprehension
    #     users = User.objects.all()
    #     results = []
    #     for user in users:
    #         post_list=[(post.title, post.content, post.created_at) for post in user.post_set.all()]
    #         results.append(
    #             {
    #                 "user" : user.name,
    #                 "post" : post_list
                    
    #             }
    #         )

    #     results = [({"user":user.name, "post":[(post.title, post.content, post.created_at) for post in user.post_set.all()]}) for user in User.objects.all()]












# results= [ 
#     ("user":user.name, 
#     "post": [(post.title, post.content, post.created_at) for post in user.post_set.all()])
#     for user in User.objects.all()
# ]
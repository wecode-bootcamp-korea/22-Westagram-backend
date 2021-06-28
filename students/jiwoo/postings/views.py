from django.shortcuts import render

# Create your views here.
class CreatePostsView(View):
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.get(name=data['user'])
        
        Post.objects.create(
            user=user,
            title = data['title'],
            content = data['content'],
            image_url = data['image_url']

        )
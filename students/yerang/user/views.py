import json

from django.http  import JsonResponse
from django.views import View

from user.models     import User
from user.validation import email_validate, password_validate

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        if not (data['email'] and data['password'] and data['phone_number'] and data['nickname']):
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        if not email_validate(data['email']):
            return JsonResponse({'message': 'INVALID_EMAIL'}, status=400)

        if not password_validate(data['password']):
            return JsonResponse({'message': 'PASSWORD_TOO_SHORT'}, status=400)

        if User.objects.filter(email=data['email']).exists():
            return JsonResponse({'message': 'EMAIL_ALREADY_EXISTS'}, status=400)
        
        if User.objects.filter(phone_number=data['phone_number']).exists():
            return JsonResponse({'message': 'PHONENUMBER_ALREADY_EXISTS'}, status=400)
        
        if User.objects.filter(nickname=data['nickname']).exists():
            return JsonResponse({'message': 'NICKNAME_ALREADY_EXISTS'}, status=400)
        
        User.objects.create(
            email        = data['email'],
            password     = data['password'],
            phone_number = data['phone_number'],
            nickname     = data['nickname'],
        )

        return JsonResponse({'message': 'SUCCESS'}, status=201)

class LikedPostView(View):
    def get(self, request, user_id):
        if not User.objects.filter(id=user_id):
            return JsonResponse({'message': 'USER_DOES_NOT_EXISTS'}, status=400)

        results = []
        user = User.objects.get(id=user_id)
        count = user.liked_posts.count()

        for liked_post in user.liked_posts.all():
            results.append(
                {
                    'post_id'  : liked_post.id,
                    'image_url': liked_post.image_url,
                }
            )
        
        return JsonResponse({f'{user.nickname} 님은 {count}개의 게시물을 좋아합니다.': results}, status=200)

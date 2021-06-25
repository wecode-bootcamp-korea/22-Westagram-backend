from django.urls import path

from users.views import UserSignUp

urlpatterns = [
    path("/signup", UserSignUp.as_view())
]

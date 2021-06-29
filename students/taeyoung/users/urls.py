from django.urls import path
from .views import AccountView, SignInView
 
urlpatterns = [
    path('/signup', AccountView.as_view()),
    path('/signin', SignInView.as_view())
]

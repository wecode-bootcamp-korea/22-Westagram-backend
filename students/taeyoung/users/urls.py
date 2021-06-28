from django.urls import path
from .views import AccountView
 
urlpatterns = [
    path('/signup', AccountView.as_view()),
    path('/signin', AccountView.as_view())
]

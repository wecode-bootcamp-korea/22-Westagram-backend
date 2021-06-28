from django.urls import path
from .views import AccountView
 
urlpatterns = [
    path('/signup', AccountView.as_view())
]


from django.urls import path
from signup.views import USERVIEW


urlpatterns = [
    path('/user',USERVIEW.as_view())
]
from django.urls import path
from user.views import UserView

urlpatterns = [path("/join", UserView.as_view())]

from django.urls import path
from users.views import SignupsView

urlpatterns = [
    path('/signup', SignupsView.as_view())
]
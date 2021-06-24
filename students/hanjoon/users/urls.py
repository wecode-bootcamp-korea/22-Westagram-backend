from django.urls import path
from users.views import StargramView

urlpatterns = [
	path('/user', StargramView.as_view()),
	]

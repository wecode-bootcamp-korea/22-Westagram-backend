from django.urls import path

from users.views import StargramView

urlpatterns = [
	path('/signup', StargramView.as_view()),
]
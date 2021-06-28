from django.urls import path

from users.views import SingupView, LoginView

urlpatterns = [
	path('/signup', SingupView.as_view()),
]
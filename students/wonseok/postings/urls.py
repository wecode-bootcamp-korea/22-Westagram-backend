from django.urls import path

from postings.views import RegisterPostView, ShowPostView

urlpatterns = [
    path("/register", RegisterPostView.as_view()),
    path("/show", ShowPostView.as_view())
]
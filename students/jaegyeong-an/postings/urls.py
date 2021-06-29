from django.urls    import path

from postings.views import WriteView, PostingsView

urlpatterns = [
    path('/write', WriteView.as_view()),
    path('/postings', PostingsView.as_view()),
    ]
from django.urls    import path

from postings.views import WriteView, PostingsView, CommentsView

urlpatterns = [
    path('/write', WriteView.as_view()),
    path('/postings', PostingsView.as_view()),
    path('/postings/<int:posting_id>', CommentsView.as_view()),
    ]
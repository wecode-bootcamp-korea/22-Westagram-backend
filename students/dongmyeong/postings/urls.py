from django.urls    import path

from postings.views import PostingView, CommentView

urlpatterns = [
    path('',          PostingView.as_view()),
    path('/comments', CommentView.as_view()),
]

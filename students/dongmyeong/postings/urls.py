from django.urls    import path

from postings.views import PostingView, CommentView

urlpatterns = [
        path('',                           PostingView.as_view()),
        path('/<int:posting_id>/comments', CommentView.as_view()),
        ]


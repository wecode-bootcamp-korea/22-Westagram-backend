from django.urls    import path

from postings.views import LikeView, PostingView, CommentView

urlpatterns = [
        path(''                                            , PostingView.as_view()),
        path('/<int:posting_id>'                           , PostingView.as_view()),
        path('/<int:posting_id>/comments'                  , CommentView.as_view()),
        path('/<int:posting_id>/comments/<int:comment_id>' , CommentView.as_view()),
        path('/<int:posting_id>/likes'                     , LikeView.as_view()),
        ]


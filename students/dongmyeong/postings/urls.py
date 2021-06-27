from django.urls    import path

from postings.views import LikeView, PostingView, CommentView, RecommentView

urlpatterns = [
        path(''                                                                 , PostingView.as_view()),
        path('/<int:posting_id>'                                                , PostingView.as_view()),
        path('/<int:posting_id>/comments'                                       , CommentView.as_view()),
        path('/<int:posting_id>/comments/<int:comment_id>'                      , CommentView.as_view()),
        path('/<int:posting_id>/recomments/<int:comment_id>'                    , RecommentView.as_view()),
        path('/<int:posting_id>/recomments/<int:comment_id>/<int:recomment_id>' , RecommentView.as_view()),
        path('/<int:posting_id>/likes'                                          , LikeView.as_view()),
        ]


from django.urls        import path
from accounts.views     import SignInView

urlpatterns =[
    path('/signin', SignInView.as_view())
]
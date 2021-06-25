from django.urls import path
from users.views import SignupsView

urlpatterns = [
    path('', SignupsView.as_view())
]
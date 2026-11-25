from django.urls import path
from rest_framework.authtoken import views

from user_auth_app.api.views import CreateUserView

urlpatterns = [
    path("register/", CreateUserView.as_view()),
    path("login/", views.obtain_auth_token),
]

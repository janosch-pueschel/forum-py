from rest_framework import generics
from rest_framework.authtoken.admin import User
from rest_framework.permissions import AllowAny

from user_auth_app.api.serializers import RegistrationSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

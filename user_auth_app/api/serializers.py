from rest_framework import serializers
from rest_framework.authtoken.admin import User


class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "repeated_password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        """
        Check that repeated_password matches password
        """
        if data["repeated_password"] != data["password"]:
            raise serializers.ValidationError(
                "Repeated password does not match password."
            )

        return data

    def validate_email(self, value):
        """
        Chaeck the the email address is unique.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email address already in use.")

        return value

    def create(self, validated_data):
        validated_data.pop("repeated_password")
        return User.objects.create_user(**validated_data)

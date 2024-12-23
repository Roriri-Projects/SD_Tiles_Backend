from rest_framework import serializers
from apps.ACCESS.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"},
    )
    access_token = serializers.SerializerMethodField(read_only=True)
    refresh_token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "identity",
            "access_token",
            "refresh_token",
        ]
        extra_kwargs = {
            "email": {"required": True, "max_length": 150},
            "identity": {"required": True},
        }

    def create(self, validated_data):
        """Create a new user and hash the password."""
        email = validated_data.pop("email")
        password = validated_data.pop("password")

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": "A user with this email already exists."}
            )

        user = User.objects.create_user(email=email, **validated_data)
        user.set_password(password)
        user.save()
        return user

    def get_access_token(self, obj):
        """Generate the access token for the user."""
        refresh = RefreshToken.for_user(obj)
        return str(refresh.access_token)

    def get_refresh_token(self, obj):
        """Generate the refresh token for the user."""
        refresh = RefreshToken.for_user(obj)
        return str(refresh)

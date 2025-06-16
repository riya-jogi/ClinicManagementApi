from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'email', 'name', 'password','is_admin']
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        if not check_password(data['password'], user.password):
            raise serializers.ValidationError("Invalid email or password")
        print(user)
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


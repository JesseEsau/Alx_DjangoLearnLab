from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email',
                  'bio', 'profile_picture', 'followers']


class RegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Generate the token for the user
        token, created = Token.objects.create(user=user)
        user.token = token.key
        return user

    # def create(self, validated_data):
    #     user = CustomUser(
    #         username=validated_data['username'],
    #         email=validated_data['email']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

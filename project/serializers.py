from rest_framework import serializers

from rest_framework.serializers import (ModelSerializer)

from .models import MyUser


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['email', 'password']
    def create(self, validated_data):
        return MyUser.objects.create_user(email=validated_data['email'], password=validated_data['password'])


class SigninSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

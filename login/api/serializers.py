from rest_framework import serializers
from login.models import LoginPage


class LoginPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginPage
        fields = ('fullname','email','password','confirm_password','nickname','address','phone_number',)
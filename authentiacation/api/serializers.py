from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import serializers,status
from authentiacation.models import User
from rest_framework.response import Response


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 4,
        min_length=4,
        write_only = True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields =[
            'username',
            'password',
            'token'
        ]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=4)
    last_login = serializers.CharField(max_length =255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError('A username is required to login')
        if password is None:
            raise serializers.ValidationError('A password is required to login')
        
        user = authenticate(username = username, password=password)

        if user is None:
            raise serializers.ValidationError('등록되지 않은 유저입니다.')
        if not user.is_active:
            raise serializers.ValidationError('등록되지 않은 유저입니다.')
        
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])

        return{
            'username':user.username,
            'last_login':user.last_login,
            'password':user.password,
            # 토큰 대신 사용할 password는 user.password로 값 반환됩니다 !
            'token':user.token,
        }
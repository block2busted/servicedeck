import datetime
from django.utils import timezone

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.reverse import reverse as api_reverse

from django.contrib.auth import get_user_model

from employee.models import Employee


User = get_user_model()

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA


class UserPublicSerializer(serializers.ModelSerializer):
    """"""
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'uri'
        ]

    def get_uri(self, object):
        request = self.context.get('request')
        return api_reverse('api-user:user-detail', kwargs={'username': object.username}, request=request)


class UserSingUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'token',
            'expires',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_expires(self, object):
        return timezone.now() - expire_delta + datetime.timedelta(seconds=300)

    def validate_username(self, value):
        user_qs = User.objects.filter(username=value)
        if user_qs.exists():
            raise serializers.ValidationError('User with this username is already exists.')
        return value

    def validate_email(self, value):
        user_qs = User.objects.filter(email=value)
        if user_qs.exists():
            raise serializers.ValidationError('User with this email is already exists.')
        return value

    def validate_passwords(self, data):
        password = data.get('password')
        password2 = data.pop('password2')
        if password != password2:
            raise serializers.ValidationError('Passwords must match.')
        return data

    def get_token(self, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def get_status(self, value):
        return value

    def create(self, validated_data):
        user_obj = User(
            username=validated_data.get('username'),
            email=validated_data.get('email')
        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_active = False
        user_obj.save()
        return user_obj

from django.contrib.auth import get_user_model
from rest_framework import serializers
from employee.models import Employee
from accounts.api.serializers import UserPublicSerializer
from rest_framework.reverse import reverse as api_reverse

from accounts.api.serializers import UserSingUpSerializer


class EmployeeSignUpSerializer(serializers.ModelSerializer):
    user = UserSingUpSerializer(required=True)

    class Meta:
        model = Employee
        fields = [
            'pk',
            'user',
            'first_name',
            'middle_name',
            'last_name',
            'photo',
            'position',
            'kpi',
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSingUpSerializer.create(UserSingUpSerializer(), validated_data=user_data)
        employee = Employee.objects.create(
            user=user,
            **validated_data
        )
        employee.save()
        return employee


class EmployeeInlineUserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Employee
        fields = [
            'pk',
            'user',
            'first_name',
            'middle_name',
            'last_name',
            'photo',
            'position',
            'kpi',
            'uri'
        ]
        read_only_fields = ['user']

    def get_uri(self, object):
        request = self.context.get('request')
        return api_reverse('api-employee:employee-detail', kwargs={'pk': object.pk}, request=request)


class EmployeeSerializer(serializers.ModelSerializer):
    """"""
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = [
            'pk',
            'user',
            'first_name',
            'middle_name',
            'last_name',
            'photo',
            'position',
            'kpi',
        ]
        read_only_fields = ['user']

    def validate(self, data):
        first_name = data.get('first_name', None)
        middle_name = data.get('middle_name', None)
        last_name = data.get('last_name', None)
        kpi = data.get('kpi', None)
        if first_name is None or middle_name is None or last_name is None or kpi is None:
            raise serializers.ValidationError('Enter all required fields.')
        return data

    def get_uri(self, object):
        request = self.context.get('request')
        return api_reverse('api-employee:employee-detail', kwargs={'pk': object.pk}, request=request)

from rest_framework import serializers
from employee.models import Employee
from accounts.api.serializers import UserPublicSerializer
from rest_framework.reverse import reverse as api_reverse


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

    def validate_first_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Your name is too short...')
        return value

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
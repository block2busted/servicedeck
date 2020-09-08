from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from employee.api.serializers import EmployeeInlineUserSerializer


User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    """"""
    uri = serializers.SerializerMethodField(read_only=True)
    employee_list = EmployeeInlineUserSerializer(source='employee_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'uri',
            'employee_list'
        ]

    def get_uri(self, object):
        request = self.context.get('request')
        return api_reverse('api-user:user-detail', kwargs={'username': object.username}, request=request)

    #def get_employee_list(self, object):
    #    qs = object.employee_set.all()
    #    request = self.context.get('request')
    #    return EmployeeInlineUserSerializer(qs, many=True, context={'request': request}).data
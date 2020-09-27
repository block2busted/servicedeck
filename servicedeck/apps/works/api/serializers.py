from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from works.models import Work, EmployeeWork
from employee.api.serializers import EmployeeSerializer


class WorkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = [
            'pk',
            'title',
            'important',
            'type',
            'description',
            'created',
            'due_date',
        ]


class WorkListSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Work
        fields = [
            'pk',
            'title',
            'important',
            'type',
            'description',
            'is_active',
            'status',
            'created',
            'due_date',
            'uri'
        ]

    def get_uri(self, object):
        request = self.context.get('request')
        return api_reverse('api-work:work-detail', kwargs={'pk': object.pk}, request=request)


class WorkEmployeeSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    work = WorkListSerializer()

    class Meta:
        model = EmployeeWork
        fields = [
            'pk',
            'employee',
            'work'
        ]

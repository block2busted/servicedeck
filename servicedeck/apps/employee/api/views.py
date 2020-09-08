import json

from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.shortcuts import get_object_or_404

from .serializers import EmployeeSerializer
from .paginations import EmployeePagination
from employee.models import Employee


def is_json(json_data):
    """"""
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


from accounts.api.permissions import IsOwnerOrReadOnly


class EmployeeDetailAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        return serializer.save()

    def perform_destroy(self, instance):
        if instance is not None:
            return instance.delete()
        return None


class EmployeeListAPI(
    mixins.CreateModelMixin,
    generics.ListAPIView
):
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        authentication_classes = [SessionAuthentication, JSONWebTokenAuthentication]
        pagination_class = EmployeePagination
        serializer_class = EmployeeSerializer

        queryset = Employee.objects.all()
        passed_pk = None
        search_fields = ['user__username', 'first_name', 'middle_name', 'last_name']
        ordering_fields = ['user__username', 'kpi']

        def perform_create(self, serializer):
            serializer.save(user=self.request.user)

        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)


class EmployeeCRUDAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView
):
    permission_classes = []
    authentication_classes = []
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    passed_pk = None

    def get_queryset(self):
        qs = Employee.objects.all()
        return qs

    def get_object(self):
        pk = self.request.GET.get('pk', None) or self.passed_pk
        queryset = self.get_queryset()
        obj = None
        if pk is not None:
            obj = get_object_or_404(queryset, pk=pk)
            self.check_object_permissions(self.request, obj)
        return obj

    def perform_destroy(self, instance):
        if instance is not None:
            return instance.delete()
        return None

    def get(self, request, *args, **kwargs):
        url_passed_pk = self.request.GET.get('pk', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_pk = json_data.get('pk', None)
        passed_pk = url_passed_pk or new_passed_pk or None
        self.passed_pk = passed_pk
        if passed_pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return super(EmployeeCRUDAPIView, self).get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        url_passed_pk = request.GET.get('pk', None)
        json_data = {}
        if is_json(request.body):
            json_data = json.loads(request.body)
        new_passed_pk = json_data.get('pk', None)
        requested_pk = request.data.get('pk')
        passed_pk = url_passed_pk or new_passed_pk or requested_pk or None
        self.passed_pk = passed_pk
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        pk = self.request.GET.get('pk', None)
        json_data = {}
        if is_json(request.body):
            json_data = json.loads(request.body)
        new_pk = json_data.get('pk')
        print(json_data, new_pk)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        pk = self.request.GET.get('pk', None)
        json_data = {}
        if is_json(request.body):
            json_data = json.loads(request.body)
        new_pk = json_data.get('pk')
        print(json_data, new_pk)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, pagination
from .serializers import UserDetailSerializer
from employee.api.serializers import EmployeeInlineUserSerializer
from employee.models import Employee

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'username'


class UserEmployeeAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EmployeeInlineUserSerializer
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get('username', None)
        if username is None:
            return Employee.objects.none()
        return Employee.objects.filter(user__username=username)

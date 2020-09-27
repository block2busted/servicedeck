from rest_framework import generics
from .serializers import CustomerSignUpSerializer


class CustomerSignUpAPIView(generics.CreateAPIView):
    serializer_class = CustomerSignUpSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save()
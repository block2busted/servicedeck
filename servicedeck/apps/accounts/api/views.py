from django.contrib.auth import get_user_model, authenticate
from django.db.models import Q
from rest_framework_jwt.settings import api_settings

from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSingUpSerializer
from .user.serializers import UserDetailSerializer
from .permissions import AnonPermissionOnly
User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class AuthAPIVew(APIView):
    permission_classes = [AnonPermissionOnly]

    def post(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated!'}, status=200)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        user_qs = User.objects.filter(
            Q(username=username)|
            Q(email=username)
        )
        if user_qs.count() == 1:
            user_obj = user_qs.first()
            if user_obj.check_password(password):
                user = user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response_data = jwt_response_payload_handler(token=token, user=user, request=request)
                return Response(response_data)
        else:
            return Response({'detail': 'Invalid username or password'}, status=401)


class SignUpAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSingUpSerializer
    permission_classes = [AnonPermissionOnly]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}

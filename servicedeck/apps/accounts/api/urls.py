from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import AuthAPIVew, SignUpAPIView, SignUp


urlpatterns = [
    path('jwt/', obtain_jwt_token),
    path('jwt/refresh/', refresh_jwt_token),
    path('auth/', AuthAPIVew.as_view()),
    path('sign_up/', SignUpAPIView.as_view()),
    path('signup/', SignUp.as_view())
]
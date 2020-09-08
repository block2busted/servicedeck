import datetime
from django.utils import timezone

from rest_framework_jwt.settings import api_settings


def jwt_response_payload_handler(token, user=None, request=None):
    expire_date = api_settings.JWT_REFRESH_EXPIRATION_DELTA
    return {
        'token': token,
        'user': user.username,
        'expire': timezone.now() + expire_date - datetime.timedelta(seconds=300)
    }
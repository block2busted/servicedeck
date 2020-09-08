from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/shop/', include(('shop.api.urls', 'api-shop'), namespace='api-shop')),

    path('api/employee/', include(('employee.api.urls', 'api-employee'), namespace='api-employee')),
    path('api/accounts/', include(('accounts.api.urls', 'api-accounts'), namespace='api-accounts')),
    path('api/user/', include(('accounts.api.user.urls', 'api-user'), namespace='api-user')),
]

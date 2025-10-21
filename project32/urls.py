from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include allauth URLs for social login
    path('accounts/', include('allauth.urls')),
    path('api/auth/', include('authentication.urls')),
    path('api/users/', include('users.urls')),
]

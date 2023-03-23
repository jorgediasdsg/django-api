from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')), #noqa E501
    path('admin/', admin.site.urls),
]

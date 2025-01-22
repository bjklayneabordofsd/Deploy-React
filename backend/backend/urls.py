from django.contrib import admin
from django.urls import path

from backend.views import hello_world

urlpatterns = [
    path('api/hello-world/', hello_world),
    path('admin/', admin.site.urls),
]
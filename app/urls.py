"""
URL Configuration for the Django Application.

This module defines the URL routing for the application.
The `urlpatterns` list maps URLs to views.

For more information on Django's URL routing, refer to the documentation:
    https://docs.djangoproject.com/en/stable/topics/http/urls/

Examples:
1. Function-based views:
    - Import the view: from my_app import views
    - Add a URL pattern: path('', views.home, name='home')

2. Class-based views:
    - Import the view: from other_app.views import Home
    - Add a URL pattern: path('', Home.as_view(), name='home')

3. Including other URL configurations:
    - Import the include function: from django.urls import include, path
    - Add a URL pattern: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Calendar Api",
        default_version="v1",
        description="API endpoints for Calendar",
        contact=openapi.Contact(email="api.imperfect@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin site URL
    path("admin/", admin.site.urls),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    # User-related API endpoints
    path("api/user/", include("core_apps.users.urls")),
    path("api/events/", include("core_apps.events.urls")),
]

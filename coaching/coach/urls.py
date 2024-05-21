from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.contrib import admin

app_name = "coach"

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.sign_in, name="login"),
    path("signup", views.sign_up, name="signup"),
    path("dashboard", views.dashboard, name="dashboard"),

]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.contrib import admin

app_name = "coach"

urlpatterns = [
    path("", views.home, name="home"),
    path("signin", views.sign_in, name="signin"),
    path("signup", views.sign_up, name="signup"),
    path("session", views.session, name="session"),
    path("shop", views.shop, name="shop"),
    path("products", views.products, name="products"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("session_creation", views.session_creation, name="session_creation"),

]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


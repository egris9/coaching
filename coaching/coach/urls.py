from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.contrib import admin

app_name = "coach"

urlpatterns = [
    path("", views.home, name="home"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("logout", views.sign_out, name="logout"),
    path("session", views.session, name="session"),
    path("shop", views.shop, name="shop"),
    path("products", views.products, name="products"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("session_creation", views.session_creation, name="session_creation"),
    path("addimg", views.add_session, name="addimg"),
    path("update_session", views.update_session, name="update_session"),
    path("updateimg", views.update_session_img, name="updateimg"),

]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


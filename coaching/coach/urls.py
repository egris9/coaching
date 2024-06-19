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
    path("stats", views.stats, name="stats"),
    path("shop", views.shop, name="shop"),
    path("products/<int:id>", views.products, name="products"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("session_creation", views.session_creation, name="session_creation"),
    path("addimg", views.add_session, name="addimg"),
    path("update_session", views.update_session, name="update_session"),
    path("updateimg", views.update_session_img, name="updateimg"),

    path('products_list', views.product_list, name='product_list'),
    path("cart", views.cart, name="cart"),
    path("cart/add_to_cart", views.add_to_cart, name="add_cart_item"),
    path(
        "cart/add_order",
        views.add_order_handler,
        name="add_order",
    ),
    path(
        "cart/delete_cart_item", views.delete_cart_item_handler, name="delete_cart_item"
    ),
     path("profile", views.profile, name="profile"),
     path("delete-session/<int:session_id>/", views.delete_session, name="delete_session"),
     path('products/', views.session_filtre, name='session_filtre'),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


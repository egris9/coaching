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
    path('products/', views.session_filtre, name='session_filtre'),
    path("shop", views.shop, name="shop"),
    path("products/<int:id>", views.products, name="products"),
    path('products_list', views.product_list, name='product_list'),
    

    path("session_creation", views.session_creation, name="session_creation"),
    path("update_session", views.update_session, name="update_session"),
    path("addimg", views.add_session, name="addimg"),
    path("updateimg", views.update_session_img, name="updateimg"),


    path("cart", views.cart, name="cart"),
    path(
        "cart/update_item_quantity",
        views.update_item_quantity,
        name="update_item_quantity",
    ),
    path("cart/add_to_cart", views.add_to_cart, name="add_cart_item"),
    path(
        "cart/add_order",
        views.add_order_handler,
        name="add_order",
    ),
    path(
        "cart/delete_cart_item", views.delete_cart_item_handler, name="delete_cart_item"
    ),
    path("add_to_cart_popup/<int:session_id>/", views.pop_up, name="add_to_cart_popup"),
    path("reviews/<int:session_id>/", views.reviews, name="reviews"),
    path("comments/<int:session_id>/", views.get_sessions_reviews, name="comments"),


    path("dashboard", views.dashboard, name="dashboard"),
    path("delete-session/<int:session_id>/", views.delete_session, name="delete_session"),
    path("stats", views.stats, name="stats"),
    path("stats/participent_by_coach", views.participent_by_coach, name="participent_by_coach"),
    path("stats/revenue_by_session", views.revenue_by_session, name="revenue_by_session"),
    path("stats/top_sessions", views.top_sessions, name="top_sessions"),
    path("profile", views.profile, name="profile"),
    path("profile/coach_request", views.coach_request, name="coach_request"),
    path("delete-session-order/<int:order_id>/", views.delete_session_order, name="delete_order_session"),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("auth/", obtain_auth_token),
    path("home", views.api_home),
    path("post/", views.post_list_create_view),
    path("post/<int:pk>/update/", views.post_update_view),
    path("post/<int:pk>/delete/", views.post_destroy_view),
    path("post/<int:pk>", views.post_detail_view),
]
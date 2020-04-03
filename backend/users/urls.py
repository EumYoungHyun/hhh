from django.urls import path
from django.conf.urls import url
from .views import UserViewSet

from users import views

user_list = UserViewSet.as_view({"get": "list", "post": "create"})

urlpatterns = [
    path("userList/", user_list, name="user-list"),
    path("userAdd/", user_list, name="user-add"),
]

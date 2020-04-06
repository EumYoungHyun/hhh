from django.urls import path
from .views import UserViewSet

user_list = UserViewSet.as_view({"get": "list", "post": "create"})

urlpatterns = [
    path("", user_list, name="user-list"),
]

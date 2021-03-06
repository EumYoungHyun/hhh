from django.urls import path
from .views import CommentViewSet

comment_list = CommentViewSet.as_view({"get": "list", "post": "create"})

urlpatterns = [
    path("", comment_list, name="comment-list"),
]

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from api.serializers import PostSerializer
from blog.models import Post
from api.permissions import AuthorModifyOrReadOnly
from rest_framework import permissions
from api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [AuthorModifyOrReadOnly]
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

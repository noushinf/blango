from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from blango_auth.models import User
from api.serializers import PostSerializer
from blog.models import Post
from api.permissions import AuthorModifyOrReadOnly
from rest_framework import permissions
from api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from api.serializers import PostSerializer, UserSerializer, PostDetailSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [AuthorModifyOrReadOnly]
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly |
                          IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

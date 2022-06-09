from django.shortcuts import get_object_or_404
from rest_framework import viewsets, exceptions, permissions, filters, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny

from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer
)
from posts.models import Post, Group, Follow
from .permissions import AuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    "Вьюсет для постов."
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        "Создание постов."
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    "Вьюсет для групп."
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        raise exceptions.MethodNotAllowed(
            'Метод не разрешен.'
        )

    def perform_update(self, serializer):
        raise exceptions.MethodNotAllowed(
            'Метод не разрешен.'
        )

    def perform_destroy(self, instance):
        raise exceptions.MethodNotAllowed(
            'Метод не разрешен.'
        )


class CommentViewSet(viewsets.ModelViewSet):
    "Вьюсет для комментариев."
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        pk_post = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=pk_post)
        return post.comments.all()

    def perform_create(self, serializer):
        pk_post = self.kwargs.get('post_id')
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=pk_post)
        )


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )

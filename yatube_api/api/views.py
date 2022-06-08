from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import exceptions
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer
)
from posts.models import Post, Group, Follow
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import permissions
from rest_framework import filters


class PostViewSet(viewsets.ModelViewSet):
    "Вьюсет для постов."
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.'
            )
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.'
            )
        super(PostViewSet, self).perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    "Вьюсет для групп."
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    "Вьюсет для комментариев."
    serializer_class = CommentSerializer

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

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.'
            )
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.'
            )
        super(CommentViewSet, self).perform_destroy(instance)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    pagination_class = None
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if self.request.user == serializer.validated_data['following']:
            raise exceptions.ParseError(detail='Нельзя подписаться на себя.')
        if Follow.objects.filter(
            user=self.request.user,
            following=serializer.validated_data['following']
        ).exists():
            raise exceptions.PermissionDenied(
                'Вы уже подписаны.'
            )
        else:
            serializer.save(
                user=self.request.user,
            )

    def perform_update(self, serializer):
        raise exceptions.PermissionDenied(
            'Метод не разрешен.'
        )

    def perform_destroy(self, instance):
        raise exceptions.PermissionDenied(
            'Метод не разрешен.'
        )

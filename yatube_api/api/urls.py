from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', views.CommentViewSet,
                basename='comments')
router.register(r'groups', views.GroupViewSet, basename='groups')
router.register(r'follow', views.FollowViewSet, basename='follows')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]

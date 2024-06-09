from django.urls import path
from .views import VideoListCreate, VideoDetail, video_stream

urlpatterns = [
    path('', VideoListCreate.as_view(), name='video-list-create'),
    path('<int:pk>/', VideoDetail.as_view(), name='video-detail'),
    path('stream/<int:pk>/', video_stream, name='video-stream'),
]

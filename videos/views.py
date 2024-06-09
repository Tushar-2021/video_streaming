from rest_framework import generics, permissions, filters
from django.shortcuts import render
from django.http import StreamingHttpResponse
from threading import Thread
import cv2
from .models import Video
from .serializers import VideoSerializer

class VideoListCreate(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

class VideoStreamThread(Thread):
    def __init__(self, video_url):
        self.video_url = video_url
        self.cap = cv2.VideoCapture(video_url)
        super().__init__()

    def run(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            ret, jpeg = cv2.imencode('.jpg', frame)
            self.frame = jpeg.tobytes()

def video_stream(request, pk):
    video = Video.objects.get(pk=pk)
    stream_thread = VideoStreamThread(video.url)
    stream_thread.start()

    def generate():
        while True:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + stream_thread.frame + b'\r\n\r\n')

    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')

from django.urls import include, path

urlpatterns = [
    path('api/accounts/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('videos.urls')),
]

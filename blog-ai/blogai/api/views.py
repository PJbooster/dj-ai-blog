from .models.post import Post
from django.http import JsonResponse
from rest_framework import generics, permissions

from api.serializers import PostSerializer

# Create your views here.

def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "hi there"})


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

post_list_create_view = PostListCreateAPIView.as_view()

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


post_detail_view = PostDetailAPIView.as_view()

class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

post_update_view = PostUpdateAPIView.as_view()

class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

post_destroy_view = PostDestroyAPIView.as_view()
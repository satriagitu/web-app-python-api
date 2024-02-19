from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, PostListSerializer
from rest_framework.response import Response

from rest_framework import status
# from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostRetriveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    
class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response("Success Delete Data")

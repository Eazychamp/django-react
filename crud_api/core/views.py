from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 
from .models import Post, PostComment
from .serializers import PostSerializer, CommentsSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserCreate(APIView):

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def post(self, request, format='json'):
    #     return Response('hello')


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = PostComment.objects.all()
    serializer_class = CommentsSerializer

class CommentDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = PostComment.objects.all()
    serializer_class = CommentsSerializer
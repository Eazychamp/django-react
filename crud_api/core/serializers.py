from rest_framework import serializers
from .models import Post, PostComment
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:        
        model = PostComment        
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'author', 'comments')
        model = Post

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=4, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


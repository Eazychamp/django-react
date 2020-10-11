from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 
from .views import PostDetail, PostList, PostCreate, CommentCreate, CommentDetail, UserCreate

urlpatterns = [
    path('', PostList.as_view()),
    path('user/', UserCreate.as_view()),
    path('new/', PostCreate.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('comment/', CommentCreate.as_view()),
    path('comment/<int:pk>/', CommentDetail.as_view()),
    path('login/', obtain_auth_token, name='api_token_auth'),
]
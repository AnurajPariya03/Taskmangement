from django.urls import path
from .views import TaskViewSet, UserCredentialsAPIView, signup, login_view

urlpatterns = [
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='task-list'),
    path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='task-detail'),
    path('user/', UserCredentialsAPIView.as_view(), name='user-detail'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
]

from rest_framework import generics, permissions, status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model, authenticate, login
from .models import Task, UserCredentials
from .serializers import TaskSerializer, UserCredentialsSerializer, UserSerializer

User = get_user_model()

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserCredentialsAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserCredentialsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.credentials

    def get_queryset(self):
        return UserCredentials.objects.filter(user=self.request.user)

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

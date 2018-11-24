from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .models import Task, List
from django.contrib.auth.models import User
from .serializers import ListSerializer, TaskSerializer, UserSerializer
# Create your views here.
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({"error": "invalid data"})

    token, created = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        User.create(username=username, email=email, password=password)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

class ListView(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        return List.objects.get(id=self.kwargs["pk"])

class TaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Task.objects.filter(list=List.objects.get(id=self.kwargs["fk"]))

    def perform_create(self, serializer):
        serializer.save(list=List.objects.get(id=self.kwargs["fk"]), user=self.request.user)
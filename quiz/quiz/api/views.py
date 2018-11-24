from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import authenticate, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import UserSerializer, AdvertSerializer
from django.contrib.auth.models import User
from .models import Advert
# Create your views here.
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({"errors": "Invalid data"})
    else:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        User.objects.create(username=username, email=email, password=password)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response({"errors": "Invalid data"})

class AdvertGenList(generics.ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


class AdvertGenCreate(generics.CreateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AdvertGenDetail(generics.RetrieveAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

    def get_object(self):
        ad = Advert.objects.get(id=self.kwargs["pk"])
        ad.number_views = ad.number_views + 1
        ad.save()
        return ad

class AdvertGenUpdate(generics.UpdateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        return Advert.objects.get(id=self.kwargs["pk"])



class AdvertGenDelete(generics.DestroyAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        Advert.objects.get(id=self.kwargs["pk"])

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def adverList(request):
    ads = Advert.objects.all()
    serializer = AdvertSerializer(ads, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def advertCreate(request):
    User = Token.objects.get(key="bd245281882459aa9fbb764936af3aa47ead2215").user
    if User is not None:
        serializer = AdvertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=User.objects.first())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "you are not authenticated"})
@api_view(["GET"])
def advertDetails(request, pk):
    ad = Advert.objects.get(id=pk)
    ad.number_views = ad.number_views + 1
    ad.save()
    serializer = AdvertSerializer(ad)
    return Response(serializer.data)

@api_view(["DELETE"])
def advertDelete(request, pk):
    ad = Advert.objects.get(id=pk)
    ad.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["PUT"])
def advertUpdate(request, pk):
    ad = Advert.objects.get(id=pk)
    serializer = AdvertSerializer(instance=ad, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

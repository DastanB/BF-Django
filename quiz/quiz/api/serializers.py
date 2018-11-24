from rest_framework.serializers import ModelSerializer
from .models import Advert
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class AdvertSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Advert
        fields = ['id', 'title', 'address', 'description', 'price', 'number_views', 'user']
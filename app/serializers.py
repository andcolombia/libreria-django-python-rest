from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import user

"""Define serializers from User Custom."""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user.User
        fields = ['url', 'username', 'email','last_login','is_active','date_joined', 'groups','data_claims']
        

"""Define serializers from Group."""
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
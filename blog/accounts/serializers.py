
from django.db.models import fields
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from accounts.models import User


class UserSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=500)
    
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name',
                  'last_name', 'description')
   

    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.description = self.data.get('description') 
        user.save()
        return user


    
   
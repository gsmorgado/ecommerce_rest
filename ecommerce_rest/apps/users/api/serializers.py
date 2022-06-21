from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from apps.users.models import User

#nombre del modelo + serializar
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' #all means todos los campos, #o campos especificos ['name', 'last_name'] cuando se usa fields no se usa exclude y cuando se usa exclude no se usa fields
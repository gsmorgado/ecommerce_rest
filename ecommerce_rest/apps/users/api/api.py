from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        users_serializar = UserSerializer(users, many = True)
        return Response(users_serializar.data)
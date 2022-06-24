from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

"""
class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        users_serializar = UserSerializer(users, many = True)
        return Response(users_serializar.data)

Hay alguna diferencia entre usar una vista basada funciones y una vista basadas en clases en REST?
        si, la hay, es casi la misma diferencia que en Django normal, 
        usar funciones no es tan escalable como usar clases, 
        además que las clases proveen más funciones que ayudan a estructurar mejor tu código y 
        ayudan a utilizar otras herramientas que provee DRF, y como en todo, usar funciones estará bien dependiendo la situación que quieras resolver


    """
    #usando funciones
    #pasarle los metodos http que permite
@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method =='GET':    
        users = User.objects.all()
        users_serializar = UserSerializer(users, many = True)
        return Response(users_serializar.data)
    elif request.method== 'POST':
        users_serializar = UserSerializer(data=request.data)
        if users_serializar.is_valid():
            users_serializar.save()
            return Response(users_serializar.data)
        return Response(users_serializar.errors)

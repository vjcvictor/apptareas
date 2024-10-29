from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer

class RegisterViews(APIView):
    def post(self, request):
        #print('Registro de usuario')
        #return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
      
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#OBTENER LOS DATOS DEL USUARIO LOGEADO
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    #SOBREESCRIBIR PARA MODIFICAR LOS DATOS DEL USUARIO LOGEADO
    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)

        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
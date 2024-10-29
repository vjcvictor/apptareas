from rest_framework.viewsets import ModelViewSet
from realiza.models import Realiza
from realiza.api.serializers import RealizaSerializers


class RealizaApiViewset(ModelViewSet):
    serializer_class = RealizaSerializers
    queryset = Realiza.objects.all()
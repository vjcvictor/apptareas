from rest_framework.viewsets import ModelViewSet
from reglas.models import Regla
from reglas.api.serializers import ReglaSerializers


class ReglaApiViewset(ModelViewSet):
    serializer_class = ReglaSerializers
    queryset = Regla.objects.all()
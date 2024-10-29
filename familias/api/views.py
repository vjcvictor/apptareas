from rest_framework.viewsets import ModelViewSet
from familias.models import Familia
from familias.api.serializers import FamiliaSerializers


class FamiliaApiViewset(ModelViewSet):
    serializer_class = FamiliaSerializers
    queryset = Familia.objects.all()
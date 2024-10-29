from rest_framework.viewsets import ModelViewSet
from tarea.models import Tarea
from tarea.api.serializers import TareaSerializers


class TareaApiViewset(ModelViewSet):
    serializer_class = TareaSerializers
    queryset = Tarea.objects.all()
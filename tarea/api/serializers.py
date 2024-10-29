from rest_framework import serializers
from tarea.models import Tarea

class TareaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id_tarea' , 'nombre', 'descripcion', 'prioridad', 'frecuencia', 'id_regla', 'imagen']
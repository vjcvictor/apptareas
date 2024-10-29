from rest_framework import serializers
from realiza.models import Realiza

class RealizaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Realiza
        fields = ['id_realiza', 'id_user', 'id_tarea', 'estado', 'fecha']
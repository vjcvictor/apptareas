from rest_framework import serializers
from reglas.models import Regla

class ReglaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Regla
        fields = ['id_regla' , 'descripcion', 'id_user']
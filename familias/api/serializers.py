from rest_framework import serializers
from familias.models import Familia

class FamiliaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Familia
        fields = ['id_familia' , 'nombre', 'cantidad_integrantes']
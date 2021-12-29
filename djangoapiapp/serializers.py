from rest_framework import serializers
from .models import Apicursos

class ApicursosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apicursos
        fields = ('id', 'url', 'name', 'language', 'price')




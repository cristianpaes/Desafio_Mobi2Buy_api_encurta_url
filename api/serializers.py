from api.models import urls
from rest_framework import  serializers

class urlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = urls
        fields = '__all__'
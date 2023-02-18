from rest_framework.serializers import ModelSerializer
from api.models import Event


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

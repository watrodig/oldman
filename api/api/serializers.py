from rest_framework.serializers import ModelSerializer
from api.models import Result, Event, EventCategory


class ResultSerializer(ModelSerializer):

    class Meta:
        model = Result
        fields = '__all__'


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class EventCategorySerializer(ModelSerializer):

    class Meta:
        model = EventCategory
        fields = '__all__'

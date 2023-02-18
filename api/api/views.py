from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.serializers import ResultSerializer, EventSerializer, EventCategorySerializer
from api.models import Result, Event, EventCategory


class ResultViewSet(ViewSet):

    def list(self, request):
        queryset = Result.objects.order_by('pk')
        serializer = ResultSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Result.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ResultSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Result.objects.get(pk=pk)
        except Result.DoesNotExist:
            return Response(status=404)
        serializer = ResultSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Result.objects.get(pk=pk)
        except Result.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class EventViewSet(ViewSet):

    def list(self, request):
        queryset = Event.objects.order_by('pk')
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=404)
        serializer = EventSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class EventCategoryViewSet(ViewSet):

    def list(self, request):
        queryset = EventCategory.objects.order_by('pk')
        serializer = EventCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EventCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = EventCategory.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = EventCategorySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = EventCategory.objects.get(pk=pk)
        except EventCategory.DoesNotExist:
            return Response(status=404)
        serializer = EventCategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = EventCategory.objects.get(pk=pk)
        except EventCategory.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

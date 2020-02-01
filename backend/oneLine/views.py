from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from oneLine.models import WiseSaying
from oneLine.serializers import WiseSayingSerializer


class WiseSayingView(viewsets.ModelViewSet):
    serializer_class = WiseSayingSerializer
    queryset = WiseSaying.objects.all()

from rest_framework import serializers

from oneLine.models import WiseSaying, Board


class WiseSayingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WiseSaying
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

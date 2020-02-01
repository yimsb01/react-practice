from rest_framework import serializers

from oneLine.models import WiseSaying


class WiseSayingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WiseSaying
        fields = '__all__'

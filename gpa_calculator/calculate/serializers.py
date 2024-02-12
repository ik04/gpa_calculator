from rest_framework import serializers

class EntrySerializer(serializers.Serializer):
    credit = serializers.FloatField()
    grade = serializers.CharField()

class CalculateSerializer(serializers.Serializer):
    entries = serializers.ListField(child=EntrySerializer())

from rest_framework import serializers


class NatalChartSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField()
    time_of_birth = serializers.TimeField(required=False)
    place_of_birth = serializers.CharField(max_length=100)

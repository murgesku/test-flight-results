from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    competition = serializers.CharField(max_length=255)
    user_name = serializers.CharField(max_length=255)
    scenario = serializers.CharField(max_length=255)


class ResultSerializer(serializers.Serializer):
    position = serializers.IntegerField()
    user_name = serializers.CharField(max_length=255)
    flight_time = serializers.FloatField()
    command_name = serializers.CharField(max_length=255)


class ResponseSerializer(serializers.Serializer):
    user_result = ResultSerializer()
    other_results = ResultSerializer(many=True)

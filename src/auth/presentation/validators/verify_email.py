from rest_framework import serializers


class VerifyEmailRequestValidator(serializers.Serializer):
    email = serializers.EmailField()
    next = serializers.CharField(required=False)


class PerformVerificationValidator(serializers.Serializer):
    token = serializers.CharField()

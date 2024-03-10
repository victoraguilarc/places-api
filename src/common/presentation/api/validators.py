from rest_framework import serializers


class SearchQueryValidator(serializers.Serializer):
    search = serializers.CharField(required=False, allow_null=True)


class TenantCustomersQueryValidator(serializers.Serializer):
    search = serializers.CharField(required=False, allow_null=True)
    class_id = serializers.UUIDField(required=False, allow_null=True)
    excluded_class_ids = serializers.ListSerializer(
        child=serializers.UUIDField(required=True),
        required=False,
        allow_null=True,
    )
    include_enrollments = serializers.BooleanField(required=False)
    include_assignations = serializers.BooleanField(required=False)

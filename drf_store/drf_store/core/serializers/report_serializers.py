from rest_framework import serializers as drf_serializers

from drf_store.core.reports import ReportParams, MetricChoices


class ReportEntrySerializer(drf_serializers.Serializer):
    month = drf_serializers.DateField()
    value = drf_serializers.DecimalField(
        max_digits=4,
        decimal_places=2
    )


class ReportParamSerializer(drf_serializers.Serializer):
    start_date = drf_serializers.DateField()
    end_date = drf_serializers.DateField()
    metric = drf_serializers.ChoiceField(choices=[
        (el.value, el.value) for el in MetricChoices
    ])

    def create(self, validated_data):
        return ReportParams(**validated_data)

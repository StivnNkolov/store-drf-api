from rest_framework import views as drf_views
from rest_framework.response import Response

from drf_store.core.reports import orders_reports
from drf_store.core.serializers.report_serializers import ReportParamSerializer, ReportEntrySerializer


class OrderReportAPIView(drf_views.APIView):
    def get(self, request):
        params_serializer = ReportParamSerializer(data=request.GET)
        params_serializer.is_valid(raise_exception=True)
        params = params_serializer.save()

        data = orders_reports(params)
        serializer = ReportEntrySerializer(instance=data, many=True)
        return Response(data=serializer.data)

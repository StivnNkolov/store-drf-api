from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum

from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth, TruncYear

from drf_store.core.models import Order


@dataclass
class ReportEntry:
    month: str
    value: Decimal


@dataclass
class ReportParams:
    start_date: datetime.date
    end_date: datetime.date
    metric: str


class MetricChoices(Enum):
    price = 'price'
    count = 'count'


def find_queryset(params):
    if params.metric == MetricChoices.count.value:
        return Order.objects.annotate(
            year=TruncYear('date')
            , month=TruncMonth('date')
        ).filter(
            date__gte=params.start_date,
            date__lte=params.end_date
        ).values('year', 'month').prefetch_related('products').annotate(value=Count('products'))
    return Order.objects.annotate(
        year=TruncYear('date')
        , month=TruncMonth('date')
    ).filter(
        date__gte=params.start_date,
        date__lte=params.end_date
    ).values('year', 'month').prefetch_related('products').annotate(value=Sum('products__price'))


def orders_reports(params):
    data = []

    queryset = find_queryset(params)

    for entry in queryset:
        report_entry = ReportEntry(
            month=f'{entry["year"].strftime("%Y")} {entry["month"].strftime("%b")}',
            value=entry['value'],
        )
        data.append(report_entry)
    return data

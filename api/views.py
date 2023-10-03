from datetime import datetime, timedelta

from django.http import FileResponse
from django.db.models import Count
from django.db.models.functions import Concat

from robots.models import Robot
from .constants import TIMEDELTA_DAYS
from .utils import get_excel_file_from_queryset


def get_robots_timedelta(request):
    """
    Возвращает Excel-файл с произведенными за прошедшие дни роботами.
    Количество дней задается константой.
    """
    time_to_compare = datetime.now() - timedelta(TIMEDELTA_DAYS)
    robots_queryset = Robot.objects.filter(
        created__gte=time_to_compare
    ).values(
        'model',
        'version'
    ).annotate(
        count=Count(Concat('model', 'version'))
    ).order_by('model', 'count')
    file = get_excel_file_from_queryset(robots_queryset)
    response = FileResponse(file, filename='result.xlsx', as_attachment=True)
    return response

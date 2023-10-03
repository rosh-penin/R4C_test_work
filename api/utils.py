import json

from django.db.models import Model

from .exceptions import ValidationError


def get_fields_from_model(model: Model) -> list:
    """Отдает наименования полей модели."""
    return [field.name for field in model._meta.fields]


def get_json_from_request(request) -> dict:
    """Возвращает словарь из JSON-строки."""
    try:
        body: dict = json.loads(request.body or 'null')
    except json.decoder.JSONDecodeError:
        raise ValidationError('Запрос ожидает JSON-строку')
    return body

from django.db.models import Model

from .exceptions import ValidationError


def validate_fields(model_fields: Model, load: dict):
    """Проверяет данные из JSON-строки на соответствие полям модели."""
    for key in load.keys():
        if key not in model_fields:
            print(model_fields)
            print(key)
            raise ValidationError(f'Поле {key} указано с ошибкой.')

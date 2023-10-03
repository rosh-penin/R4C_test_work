from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .errors import return_exception
from .exceptions import ValidationError
from .validators import validate_fields
from .utils import get_fields_from_model, get_json_from_request
from robots.models import Robot


@require_POST
@csrf_exempt
def new_robots(request):
    """Создает нового робота в базе данных из полученных данных."""
    try:
        robot_from_json: dict = get_json_from_request(request)
        if not robot_from_json:
            raise ValidationError('Пустой запрос')
        model_fields = get_fields_from_model(Robot)
        validate_fields(model_fields, robot_from_json)
        robot_from_json['serial'] = (f'{robot_from_json["model"]}-'
                                     f'{robot_from_json["version"]}')
        Robot.objects.create(**robot_from_json)
    except ValidationError as e:
        return return_exception(e.message)
    return JsonResponse({'success': 'Robot was created in database'},
                        status=201)

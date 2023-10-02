from django.http import JsonResponse


def return_exception(message):
    """Возвращает JSON-ответ с сообщением ошибки и статусом 400."""
    return JsonResponse({"error": message}, status=400)

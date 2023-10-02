class ValidationError(Exception):
    """Ошибка для обозначения проблемы с валидацией данных."""
    def __init__(self, message, *args):
        self.message = message
        super().__init__(*args)

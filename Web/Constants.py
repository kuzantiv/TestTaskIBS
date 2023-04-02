class CommonConstants:
    """Данный класс объединяет константы участвующие в большинстве тестов."""
    BASE_URL: str = "https://reqres.in/"


class PageConstants:
    """Данный класс объединяет константы для тестов."""
    PAGE1: str = CommonConstants.BASE_URL + "/api/users?page=1"
    PAGE2: str = CommonConstants.BASE_URL + "/api/users?page=2"

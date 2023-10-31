import requests

from settings import SETTINGS


class GetWeatherRequest():
    """
    Выполняет запрос на получение текущей погоды для города
    """

    def __init__(self):
        """
        Инициализирует класс
        """
        self.session = requests.Session()

    def get_weather_url(self, city):
        """
        Генерирует url включая в него необходимые параметры
        Args:
            city: Город
        Returns:

        """
        url = 'https://api.openweathermap.org/data/2.5/weather'
        url += '?units=metric'
        url += '&q=' + city
        url += '&appid=' + SETTINGS.WEATHER_API_KEY
        return url

    def send_request(self, url):
        """
        Отправляет запрос на сервер
        Args:
            url: Адрес запроса
        Returns:

        """
        request = self.session.get(url)
        if request.status_code == 200:
            return request
        request.raise_for_status()

    def get_weather_from_response(self, response):
        """
        Достает погоду из ответа
        Args:
            response: Ответ, пришедший с сервера
        Returns:

        """
        return response.json()['main']['temp']

    def get_weather(self, city):
        """
        Делает запрос на получение погоды
        Args:
            city: Город
        Returns:

        """
        url = self.get_weather_url(city)
        request = self.send_request(url)
        if request:
            weather = self.get_weather_from_response(request)
            return weather
        return

class CheckCityExisting():
    """
    Проверка наличия города (запросом к серверу погоды)
    """

    def __init__(self):
        """
        Инициализирует класс
        """
        self.session = requests.Session()

    def get_weather_url(self, city):
        """
        Генерирует url включая в него необходимые параметры
        Args:
            city: Город
        Returns:

        """
        url = 'https://api.openweathermap.org/data/2.5/weather'
        url += '?units=metric'
        url += '&q=' + city
        url += '&appid=' + SETTINGS.WEATHER_API_KEY
        return url

    def send_request(self, url):
        """
        Отправляет запрос на сервер
        Args:
            url: Адрес запроса
        Returns:

        """
        return self.session.get(url)

    def check_existing(self, city):
        """
        Проверяет наличие города
        Args:
            city: Название города
        Returns:

        """
        url = self.get_weather_url(city)
        request = self.send_request(url)
        if request.status_code == 200:
            return True
        return

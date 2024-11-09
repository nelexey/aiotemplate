import aiohttp
import urllib.parse


class Service:
    """Класс для настройки и выполнения HTTP-запросов к API."""

    class ResponseError(Exception):
        def __init__(self, status: int, message: str):
            self.status = status
            self.message = message
            super().__init__(f"{status}: {message}")

    def __init__(self, url: str):
        self.url = url

    async def make_request(self, method: str = 'POST', data: dict = None, uri: str = '', r_type: str = 'text'):
        """Выполняет HTTP-запрос и возвращает результат в формате, указанном в r_type."""

        if method == 'GET' and data is not None:
            query_string = urllib.parse.urlencode(data)
            url = f"{self.url}/{uri}?{query_string}"
        else:
            url = f"{self.url}/{uri}"

        print(url)

        async with aiohttp.ClientSession() as session:
            try:
                async with session.request(method, url, json=data) as response:
                    content_type = response.headers.get("Content-Type", "")

                    if r_type == 'json' and 'application/json' in content_type:
                        return await response.json()
                    elif r_type == 'text' and 'text/plain' in content_type:
                        return await response.text()
                    elif r_type == 'read':
                        return await response.read()
                    else:
                        return response

            except aiohttp.client_exceptions.ClientConnectorError as e:
                raise self.ResponseError(status=0, message=str(e))

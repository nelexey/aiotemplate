import aiohttp
import urllib.parse

class Service:
    """"""
    class ResponseError(Exception):
        def __init__(self, status: int, message: str):
            self.status = status
            self.message = message
            super().__init__(f"{status}: {message}")

    def __init__(self, url: str):
        self.url = url

    async def make_request(self, method: str = 'POST', data: dict = None, uri: str = '') -> dict:
        if method == 'GET' and data is not None:
            query_string = urllib.parse.urlencode(data)
            url = f"{self.url}/{uri}?{query_string}"
        else:
            url = f"{self.url}/{uri}"

        async with aiohttp.ClientSession() as session:
            try:
                async with session.request(method, url, json=data) as response:
                    content_type = response.headers.get("Content-Type")
                    if "application/json" in content_type:
                        print('1', await response.json())
                        return await response.json()
                    elif "text/plain" in content_type:
                        print('2', await response.text())
                        return await response.text()
                    else:
                        print('3', await response.read())
                        return await response.read()
            except aiohttp.client_exceptions.ClientConnectorError as e:
                raise self.ResponseError

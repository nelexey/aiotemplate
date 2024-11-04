from .Service import Service

from bot.misc.env import settings

some_service = Service(settings.some_service['url'])

async def example_req(param1: int = None,
                      param2: int = None) -> dict:

    request_data = {
        'param1': param1,
        'param2': param2,
    }
    return await some_service.make_request('POST', data=request_data, uri='new_query')

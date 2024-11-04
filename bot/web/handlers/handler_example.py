import json
from aiohttp import web

async def handle_request(request):
    # Parse JSON data from the request
    try:
        data = await request.json()
    except json.JSONDecodeError:
        return web.Response(text="Invalid JSON data", status=400)

    # Validate and retrieve 'chat_id'
    chat_id = data.get('some_parameter')
    if chat_id is None:
        return web.Response(text="Missing 'some_parameter' parameter", status=400)

    response_text = "Operation completed successfully"

    # Return final response
    return web.Response(text=response_text)

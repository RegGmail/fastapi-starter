import datetime
from models.hello.hello_response_models import HelloResponse

async def resolve_hello_world ()  -> HelloResponse:
    return HelloResponse("Hello Mundo!", datetime.datetime.now())


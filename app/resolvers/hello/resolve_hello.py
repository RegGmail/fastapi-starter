import datetime
from models.hello.hello_response_models import HelloResponse

async def resolve_hello_word ()  -> HelloResponse:
    return HelloResponse("Hello Mundo!", datetime.datetime.now())


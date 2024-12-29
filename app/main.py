from fastapi import FastAPI
import uvicorn, datetime

from config import settings
print ("Passo 1")
from graphql_api import graphql_app

print ("Passo 2")
app = FastAPI()

app.mount ('/graph', graphql_app)

print ("Passo 3")

@app.on_event ('startup')
async def startup():
    public_paths = {'/', '/graph'}

print ("Passo 4")

@app.get ("/")
async def root():
    return {"message": {
        "app_name": settings.APP_NAME,
        "system_time": datetime.datetime.now()
    }}

print ("Passo 5")

if __name__ == "__main__":
    uvicorn.run (
        "main:app",
        host=settings.HOST,
        reload=True,
        port=settings.PORT
    )

'''
@app.get("/")
async def root():
    return {"message": "Alo Pessoal"}
'''

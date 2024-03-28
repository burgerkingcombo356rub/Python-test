import uvicorn
from fastapi import FastAPI

from cities.router import router as cities_router
from core.utils.logger import Logger
from picnics.router import router as picnics_router
from users.router import router as users_router

app = FastAPI()

#Routes
app.include_router(users_router)
app.include_router(picnics_router)
app.include_router(cities_router)


Logger()

if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000) pls pls pls 


Aviasales for everyone
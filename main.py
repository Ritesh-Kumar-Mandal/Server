from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server import models
from server.utils.dbUtil import engine
from server.routers import user
import uvicorn

## -------------------------------- Database connection initialization --------------------------------
models.Base.metadata.create_all(bind=engine)

## -------------------------------- App initialization --------------------------------
app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="Server Side  [Python(FastAPI)]",
    version="0.1.0",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
## -------------------------------- Register Route for {User} -------------------------------
app.include_router(user.router)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
## uvicorn main:app --reload
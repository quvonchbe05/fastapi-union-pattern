from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.users import router as user_router


app = FastAPI(
    title="Test architecture",
    version="v1",
    docs_url="/swagger"
)


app.include_router(user_router)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)

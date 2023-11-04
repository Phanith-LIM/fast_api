import uvicorn
from fastapi import FastAPI
from core.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from modules.user.controller import router as user_router

Base.metadata.create_all(bind=engine)
app = FastAPI(
    docs_url="/",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)
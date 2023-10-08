import uvicorn
from fastapi import FastAPI
from core.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from modules.users.controller import router as user_router
from modules.auth.controller import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    docs_url="/swagger",
    title="Report Management API",
    description="Report Management API",
    version="1.0.0",
    redoc_url=None,
    swagger_ui_parameters={
        "dom_id": "#swagger-ui",
        "layout": "BaseLayout",
        "deepLinking": True,
        "showExtensions": True,
        "showCommonExtensions": True,
    }
)

@app.get("/")
async def root():
    return {"message": "REPORT MANAGEMENT API"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)
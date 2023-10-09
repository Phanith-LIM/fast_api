import uvicorn
from fastapi import FastAPI
from core.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from modules.users.controller import router as user_router
from modules.auth.controller import router as auth_router
import fastapi.openapi.utils as openapi
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.security import OAuth2PasswordBearer

Base.metadata.create_all(bind=engine)


app = FastAPI(
    docs_url=None
)

@app.get("/swagger", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="FastAPI",
        swagger_favicon_url="https://cdn.svgporn.com/logos/swagger.svg",
    )

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = openapi.get_openapi(
        title="FAST-API",
        version="1.0.0",
        routes=app.routes,
        openapi_version="3.1.0",
        servers=[
            {"url": "https://test-api-602w.onrender.com"}
        ],
    )
    for path, path_item in openapi_schema["paths"].items():
        for method, operation in path_item.items():
            if "responses" in operation:
                for status_code, response in operation["responses"].items():
                    response["description"] = ""
                if "422" in operation["responses"]:
                    del operation["responses"]["422"]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/", tags=["Root"], operation_id='root')
async def root():
    return {"message": "FAST-API"}

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
    uvicorn.run(app, host='0.0.0.0', port=8000)
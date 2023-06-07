import toml as toml
from A1Task import PACKAGE_ROOT
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.middleware.cors import CORSMiddleware
from A1Task.api import user


def get_project_version() -> str:
    with open(PACKAGE_ROOT / "pyproject.toml") as f:
        pyproject_data = toml.load(f)
    return pyproject_data["tool"]["poetry"]["version"]


app = FastAPI(
    title="Startizer",
    version=get_project_version(),  # type: ignore  # noqa
)

app.include_router(user.app)

origins = []
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return RedirectResponse(url='/docs')

#videti sto je ovako
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title,
    )


if __name__ == "__main__":
    uvicorn.run(
        "A1Task.api.main:app",
        host="127.0.0.1",
        port=8001,
        log_level="debug")

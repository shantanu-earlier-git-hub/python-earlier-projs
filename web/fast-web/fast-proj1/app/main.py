import uvicorn
from starlette.responses import RedirectResponse

from app import app


@app.get("/")
async def root():
    return RedirectResponse("/home", status_code=307)


@app.get("/home")
async def root():
    return {"message": "home page"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

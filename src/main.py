from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def read_root():
    return HTMLResponse("<h1>Thumbnail Collection Pipeline</h1>", status_code=200)
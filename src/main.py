from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .collection.routers import router as collection_router

app = FastAPI()
app.include_router(collection_router)

@app.get("/")
async def read_root():
    return HTMLResponse("<h1>Thumbnail Collection Pipeline</h1>", status_code=200)
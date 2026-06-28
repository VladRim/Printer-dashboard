from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.routers.v1 import printers, cartridges, search, dashboard

app = FastAPI()

# API
app.include_router(printers.router)
app.include_router(cartridges.router)
app.include_router(search.router)

# UI
app.include_router(dashboard.router)


@app.get("/")
def root():
    return RedirectResponse(url="/dashboard")


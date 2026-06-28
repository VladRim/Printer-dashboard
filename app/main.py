from fastapi import FastAPI
from fastapi import FastAPI

from app.routers import (
    dashboard_router,
    printers_router,
    cartridges_router,
    stock_router,
    search_router,
    auth_router,
    users_router,
)

app = FastAPI(title="Printer Dashboard")

app.include_router(dashboard_router)
app.include_router(printers_router)
app.include_router(cartridges_router)
app.include_router(stock_router)
app.include_router(search_router)
app.include_router(auth_router)
app.include_router(users_router)

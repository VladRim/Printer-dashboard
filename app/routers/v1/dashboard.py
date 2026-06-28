from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services.printer_service import PrinterService
from app.services.stock_service import StockService

router = APIRouter(tags=["Dashboard"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def dashboard(
    request: Request,
    db: Session = Depends(get_db)
):
    printer_service = PrinterService(db)
    stock_service = StockService(db)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "printer_count": printer_service.count(),
            "low_stock": stock_service.low_stock_count(),
        },
    )

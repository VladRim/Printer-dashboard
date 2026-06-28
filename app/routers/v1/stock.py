from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services.stock_service import StockService

router = APIRouter(
    prefix="/stock",
    tags=["Stock"]
)


@router.get("/")
def stock(
    db: Session = Depends(get_db)
):
    return StockService(db).get_all()


@router.get("/low")
def low_stock(
    db: Session = Depends(get_db)
):
    return StockService(db).low_stock()

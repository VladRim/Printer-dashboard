from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services.printer_service import PrinterService

router = APIRouter(prefix="/printers", tags=["Printers"])

service = PrinterService()


@router.get("/")
def get_printers(db: Session = Depends(get_db)):
    return service.search_printers(db, "")


@router.get("/{printer_id}")
def get_printer(printer_id: int, db: Session = Depends(get_db)):
    return service.get_printer(db, printer_id)


@router.get("/{printer_id}/cartridges")
def get_cartridges(printer_id: int, db: Session = Depends(get_db)):
    return service.get_printer_cartridges(db, printer_id)

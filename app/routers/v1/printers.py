from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.printer import PrinterCreate
from app.services.printer_service import PrinterService

router = APIRouter(
    prefix="/printers",
    tags=["Printers"]
)


@router.get("/")
def get_printers(
    db: Session = Depends(get_db)
):
    return PrinterService(db).get_all()


@router.get("/{printer_id}")
def get_printer(
    printer_id: int,
    db: Session = Depends(get_db)
):
    return PrinterService(db).get(printer_id)


@router.post("/")
def create_printer(
    printer: PrinterCreate,
    db: Session = Depends(get_db)
):
    return PrinterService(db).create(printer)


@router.delete("/{printer_id}")
def delete_printer(
    printer_id: int,
    db: Session = Depends(get_db)
):
    return PrinterService(db).delete(printer_id)

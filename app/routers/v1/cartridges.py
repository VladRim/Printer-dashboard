from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services.cartridge_service import CartridgeService

router = APIRouter(prefix="/cartridges", tags=["Cartridges"])

service = CartridgeService()


@router.get("/")
def get_cartridges(db: Session = Depends(get_db)):
    return service.search_cartridges(db, "")


@router.get("/{cartridge_id}/printers")
def get_printers(cartridge_id: int, db: Session = Depends(get_db)):
    return service.get_printers(db, cartridge_id)

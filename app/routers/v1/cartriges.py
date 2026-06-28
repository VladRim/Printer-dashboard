from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.cartridge import CartridgeCreate
from app.services.cartridge_service import CartridgeService

router = APIRouter(
    prefix="/cartridges",
    tags=["Cartridges"]
)


@router.get("/")
def get_cartridges(
    db: Session = Depends(get_db)
):
    return CartridgeService(db).get_all()


@router.post("/")
def create_cartridge(
    cartridge: CartridgeCreate,
    db: Session = Depends(get_db)
):
    return CartridgeService(db).create(cartridge)

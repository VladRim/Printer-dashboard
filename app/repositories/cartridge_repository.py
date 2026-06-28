from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.cartridge import Cartridge
from app.models.printer_cartridge import PrinterCartridge
from app.models.printer import Printer
from app.repositories.base import BaseRepository


class CartridgeRepository(BaseRepository[Cartridge]):

    def __init__(self):
        super().__init__(Cartridge)

    # 🔎 поиск картриджей
    def search(self, db: Session, text: str):

        return (
            db.query(Cartridge)
            .filter(
                or_(
                    Cartridge.model.ilike(f"%{text}%"),
                    Cartridge.vendor.ilike(f"%{text}%"),
                )
            )
            .all()
        )

    # 🧩 картридж → принтеры
    def get_printers(self, db: Session, cartridge_id: int):

        return (
            db.query(Printer, PrinterCartridge)
            .join(PrinterCartridge)
            .join(Cartridge)
            .filter(Cartridge.id == cartridge_id)
            .all()
        )

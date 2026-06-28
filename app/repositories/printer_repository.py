from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.printer import Printer
from app.models.printer_cartridge import PrinterCartridge
from app.models.cartridge import Cartridge
from app.repositories.base import BaseRepository


class PrinterRepository(BaseRepository[Printer]):

    def __init__(self):
        super().__init__(Printer)

    # 🔎 поиск принтеров
    def search(self, db: Session, text: str):

        return (
            db.query(Printer)
            .filter(
                or_(
                    Printer.model.ilike(f"%{text}%"),
                    Printer.vendor.ilike(f"%{text}%"),
                    Printer.serial_number.ilike(f"%{text}%"),
                    Printer.inventory_number.ilike(f"%{text}%"),
                    Printer.ip_address.ilike(f"%{text}%"),
                )
            )
            .all()
        )

    # 🧩 принтер → картриджи
    def get_cartridges(self, db: Session, printer_id: int):

        return (
            db.query(Cartridge, PrinterCartridge)
            .join(PrinterCartridge)
            .join(Printer)
            .filter(Printer.id == printer_id)
            .all()
        )

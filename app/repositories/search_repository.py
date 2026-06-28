from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.printer import Printer
from app.models.cartridge import Cartridge


class SearchRepository:

    def search(self, db: Session, text: str):

        printers = (
            db.query(Printer)
            .filter(
                or_(
                    Printer.model.ilike(f"%{text}%"),
                    Printer.vendor.ilike(f"%{text}%"),
                    Printer.serial_number.ilike(f"%{text}%"),
                )
            )
            .all()
        )

        cartridges = (
            db.query(Cartridge)
            .filter(
                or_(
                    Cartridge.model.ilike(f"%{text}%"),
                    Cartridge.vendor.ilike(f"%{text}%"),
                )
            )
            .all()
        )

        return {
            "printers": printers,
            "cartridges": cartridges
        }

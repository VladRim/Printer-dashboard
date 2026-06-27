from sqlalchemy.orm import Session

from app.models.printer import Printer
from app.models.cartridge import Cartridge


class SearchRepository:

    def __init__(self, session: Session):
        self.session = session

    def search_printers(self, query: str):
        return (
            self.session.query(Printer)
            .filter(
                Printer.model.ilike(f"%{query}%")
                | Printer.serial_number.ilike(f"%{query}%")
                | Printer.inventory_number.ilike(f"%{query}%")
                | Printer.ip_address.ilike(f"%{query}%")
            )
            .all()
        )

    def search_cartridges(self, query: str):
        return (
            self.session.query(Cartridge)
            .filter(
                Cartridge.model.ilike(f"%{query}%")
            )
            .all()
        )

    def global_search(self, query: str):
        return {
            "printers": self.search_printers(query),
            "cartridges": self.search_cartridges(query),
        }

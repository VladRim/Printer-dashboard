from sqlalchemy.orm import Session

from app.models.printer import Printer
from app.repositories.base import BaseRepository


class PrinterRepository(BaseRepository[Printer]):

    def __init__(self, session: Session):
        super().__init__(Printer, session)

    def get_by_ip(self, ip: str):
        return (
            self.session.query(Printer)
            .filter(Printer.ip_address == ip)
            .first()
        )

    def search(self, query: str):
        return (
            self.session.query(Printer)
            .filter(
                Printer.model.ilike(f"%{query}%")
                | Printer.serial_number.ilike(f"%{query}%")
                | Printer.inventory_number.ilike(f"%{query}%")
            )
            .all()
        )

from sqlalchemy.orm import Session

from app.repositories.printer_repository import PrinterRepository
from app.repositories.cartridge_repository import CartridgeRepository


class PrinterService:

    def __init__(self):
        self.printer_repo = PrinterRepository()
        self.cartridge_repo = CartridgeRepository()

    # 🖨 получить принтер
    def get_printer(self, db: Session, printer_id: int):
        return self.printer_repo.get(db, printer_id)

    # 🔎 поиск принтеров
    def search_printers(self, db: Session, text: str):
        return self.printer_repo.search(db, text)

    # 🧩 принтер → картриджи (бизнес-логика)
    def get_printer_cartridges(self, db: Session, printer_id: int):

        results = self.printer_repo.get_cartridges(db, printer_id)

        # нормализация под UI
        return [
            {
                "cartridge": c.Cartridge,
                "compatibility": c.PrinterCartridge.compatibility_type,
                "priority": c.PrinterCartridge.priority,
            }
            for c in results
        ]

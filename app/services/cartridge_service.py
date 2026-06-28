from sqlalchemy.orm import Session

from app.repositories.cartridge_repository import CartridgeRepository


class CartridgeService:

    def __init__(self):
        self.repo = CartridgeRepository()

    def get_cartridge(self, db: Session, cartridge_id: int):
        return self.repo.get(db, cartridge_id)

    def search_cartridges(self, db: Session, text: str):
        return self.repo.search(db, text)

    # 🎯 cartridge → printers
    def get_printers(self, db: Session, cartridge_id: int):
        return self.repo.get_printers(db, cartridge_id)

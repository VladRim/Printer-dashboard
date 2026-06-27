from sqlalchemy.orm import Session

from app.models.cartridge import Cartridge
from app.repositories.base import BaseRepository


class CartridgeRepository(BaseRepository[Cartridge]):

    def __init__(self, session: Session):
        super().__init__(Cartridge, session)

    def search(self, query: str):
        return (
            self.session.query(Cartridge)
            .filter(
                Cartridge.model.ilike(f"%{query}%")
            )
            .all()
        )

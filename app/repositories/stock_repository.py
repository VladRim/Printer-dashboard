from sqlalchemy.orm import Session

from app.models.stock import Stock
from app.repositories.base import BaseRepository


class StockRepository(BaseRepository[Stock]):

    def __init__(self, session: Session):
        super().__init__(Stock, session)

    def get_low_stock(self):
        return (
            self.session.query(Stock)
            .filter(Stock.quantity <= Stock.minimum_quantity)
            .all()
        )

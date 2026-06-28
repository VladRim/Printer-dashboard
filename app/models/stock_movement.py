from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from datetime import datetime

from app.models.base import Base
from app.enums.stock_operation import StockOperation


class StockMovement(Base):
    __tablename__ = "stock_movement"

    id = Column(Integer, primary_key=True, index=True)

    cartridge_id = Column(Integer, ForeignKey("cartridges.id"))

    operation = Column(Enum(StockOperation))
    quantity = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)

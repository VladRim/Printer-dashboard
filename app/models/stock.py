from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, index=True)

    cartridge_id = Column(Integer, ForeignKey("cartridges.id"), unique=True)

    quantity = Column(Integer, default=0)

    cartridge = relationship("Cartridge")

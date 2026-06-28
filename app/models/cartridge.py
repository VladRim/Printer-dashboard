from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Cartridge(Base):
    __tablename__ = "cartridges"

    id = Column(Integer, primary_key=True, index=True)

    vendor = Column(String(100))
    model = Column(String(150), index=True)

    type = Column(String(50))
    color = Column(String(50))

    yield_pages = Column(Integer)
    description = Column(String(255))

    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))

    manufacturer = relationship("Manufacturer")

    printers = relationship(
        "PrinterCartridge",
        back_populates="cartridge"
    )

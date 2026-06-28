from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.enums.compatibility_type import CompatibilityType


class PrinterCartridge(Base):
    __tablename__ = "printer_cartridge"

    id = Column(Integer, primary_key=True, index=True)

    printer_id = Column(Integer, ForeignKey("printers.id"))
    cartridge_id = Column(Integer, ForeignKey("cartridges.id"))

    compatibility_type = Column(Enum(CompatibilityType))
    priority = Column(Integer, default=1)

    printer = relationship("Printer", back_populates="cartridges")
    cartridge = relationship("Cartridge", back_populates="printers")

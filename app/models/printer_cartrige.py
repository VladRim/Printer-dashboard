from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class PrinterCartridge(Base):
    __tablename__ = "printer_cartridges"

    printer_id: Mapped[int] = mapped_column(
        ForeignKey("printers.id"),
        primary_key=True
    )

    cartridge_id: Mapped[int] = mapped_column(
        ForeignKey("cartridges.id"),
        primary_key=True
    )

    is_default: Mapped[bool] = mapped_column(default=False)

    printer = relationship("Printer", back_populates="cartridges")
    cartridge = relationship("Cartridge", back_populates="printers")

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Cartridge(Base, TimestampMixin):
    __tablename__ = "cartridges"

    id: Mapped[int] = mapped_column(primary_key=True)

    manufacturer_id: Mapped[int] = mapped_column(
        ForeignKey("manufacturers.id")
    )

    model: Mapped[str] = mapped_column(String(120), index=True)

    color: Mapped[str | None] = mapped_column(String(30))
    resource: Mapped[int | None] = mapped_column(Integer)

    is_original: Mapped[bool] = mapped_column(default=True)

    manufacturer = relationship("Manufacturer", back_populates="cartridges")

    printers = relationship(
        "PrinterCartridge",
        back_populates="cartridge",
        cascade="all, delete-orphan"
    )

    stock = relationship(
        "Stock",
        back_populates="cartridge",
        cascade="all, delete-orphan"
    )

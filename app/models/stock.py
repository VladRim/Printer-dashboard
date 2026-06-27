from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Stock(Base, TimestampMixin):
    __tablename__ = "stock"

    id: Mapped[int] = mapped_column(primary_key=True)

    cartridge_id: Mapped[int] = mapped_column(
        ForeignKey("cartridges.id")
    )

    quantity: Mapped[int] = mapped_column(default=0)
    minimum_quantity: Mapped[int] = mapped_column(default=0)

    cartridge = relationship("Cartridge", back_populates="stock")

    movements = relationship(
        "StockMovement",
        back_populates="stock",
        cascade="all, delete-orphan"
    )

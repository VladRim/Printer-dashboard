from sqlalchemy import Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.enums.stock_operation import StockOperation
from app.models.base import Base, TimestampMixin


class StockMovement(Base, TimestampMixin):
    __tablename__ = "stock_movements"

    id: Mapped[int] = mapped_column(primary_key=True)

    stock_id: Mapped[int] = mapped_column(
        ForeignKey("stock.id")
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    operation: Mapped[StockOperation] = mapped_column(
        Enum(StockOperation, name="stock_operation")
    )

    quantity: Mapped[int] = mapped_column(Integer)

    comment: Mapped[str | None] = mapped_column(String(255))

    stock = relationship("Stock", back_populates="movements")
    user = relationship("User", back_populates="movements")

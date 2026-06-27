from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Manufacturer(Base, TimestampMixin):
    __tablename__ = "manufacturers"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True
    )

    printers = relationship("Printer", back_populates="manufacturer")
    cartridges = relationship("Cartridge", back_populates="manufacturer")

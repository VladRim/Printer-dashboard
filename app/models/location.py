from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Location(Base, TimestampMixin):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)

    building: Mapped[str] = mapped_column(String(50))
    floor: Mapped[str] = mapped_column(String(20))
    room: Mapped[str] = mapped_column(String(20))
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    printers = relationship("Printer", back_populates="location")

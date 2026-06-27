from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.enums.printer_status import PrinterStatus
from app.models.base import Base, TimestampMixin


class Printer(Base, TimestampMixin):
    __tablename__ = "printers"

    id: Mapped[int] = mapped_column(primary_key=True)

    manufacturer_id: Mapped[int] = mapped_column(
        ForeignKey("manufacturers.id")
    )

    department_id: Mapped[int | None] = mapped_column(
        ForeignKey("departments.id"),
        nullable=True
    )

    location_id: Mapped[int | None] = mapped_column(
        ForeignKey("locations.id"),
        nullable=True
    )

    model: Mapped[str] = mapped_column(String(120), index=True)

    serial_number: Mapped[str | None] = mapped_column(
        String(120),
        unique=True,
        nullable=True
    )

    inventory_number: Mapped[str | None] = mapped_column(
        String(120),
        unique=True,
        nullable=True
    )

    hostname: Mapped[str | None] = mapped_column(String(120))
    ip_address: Mapped[str | None] = mapped_column(String(45), index=True)
    mac_address: Mapped[str | None] = mapped_column(String(17), unique=True)

    status: Mapped[PrinterStatus] = mapped_column(
        Enum(PrinterStatus, name="printer_status"),
        default=PrinterStatus.ACTIVE
    )

    comment: Mapped[str | None] = mapped_column(String(500))

    manufacturer = relationship("Manufacturer", back_populates="printers")
    department = relationship("Department", back_populates="printers")
    location = relationship("Location", back_populates="printers")

    cartridges = relationship(
        "PrinterCartridge",
        back_populates="printer",
        cascade="all, delete-orphan"
    )

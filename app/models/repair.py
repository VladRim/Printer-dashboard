from sqlalchemy import Enum, ForeignKey, Text, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.enums.repair_status import RepairStatus
from app.models.base import Base, TimestampMixin


class Repair(Base, TimestampMixin):
    __tablename__ = "repairs"

    id: Mapped[int] = mapped_column(primary_key=True)

    printer_id: Mapped[int] = mapped_column(
        ForeignKey("printers.id")
    )

    engineer_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    problem: Mapped[str] = mapped_column(Text)
    solution: Mapped[str | None] = mapped_column(Text)

    status: Mapped[RepairStatus] = mapped_column(
        Enum(RepairStatus, name="repair_status"),
        default=RepairStatus.OPEN
    )

    printer = relationship("Printer")
    engineer = relationship("User")

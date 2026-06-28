from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Enum
from datetime import datetime

from app.models.base import Base
from app.enums.repair_status import RepairStatus


class Repair(Base):
    __tablename__ = "repairs"

    id = Column(Integer, primary_key=True, index=True)

    printer_id = Column(Integer, ForeignKey("printers.id"))

    status = Column(Enum(RepairStatus), default=RepairStatus.OPEN)

    description = Column(String(255))

    created_at = Column(DateTime, default=datetime.utcnow)
    closed_at = Column(DateTime, nullable=True)

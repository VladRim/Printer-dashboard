from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.enums.printer_status import PrinterStatus


class Printer(Base):
    __tablename__ = "printers"

    id = Column(Integer, primary_key=True, index=True)

    vendor = Column(String(100))
    model = Column(String(150), index=True)

    serial_number = Column(String(150), unique=True)
    inventory_number = Column(String(150), unique=True)

    ip_address = Column(String(45))
    mac_address = Column(String(50))

    status = Column(Enum(PrinterStatus), default=PrinterStatus.ACTIVE)

    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))
    department_id = Column(Integer, ForeignKey("departments.id"))
    location_id = Column(Integer, ForeignKey("locations.id"))

    manufacturer = relationship("Manufacturer")
    department = relationship("Department")
    location = relationship("Location")

    cartridges = relationship(
        "PrinterCartridge",
        back_populates="printer",
        cascade="all, delete-orphan"
    )

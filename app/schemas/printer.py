from typing import Optional

from pydantic import BaseModel, ConfigDict


class PrinterBase(BaseModel):
    manufacturer_id: int
    department_id: Optional[int] = None
    location_id: Optional[int] = None

    model: str
    serial_number: Optional[str] = None
    inventory_number: Optional[str] = None

    ip_address: Optional[str] = None
    mac_address: Optional[str] = None
    hostname: Optional[str] = None

    comment: Optional[str] = None


class PrinterCreate(PrinterBase):
    pass


class PrinterUpdate(BaseModel):
    manufacturer_id: Optional[int] = None
    department_id: Optional[int] = None
    location_id: Optional[int] = None

    model: Optional[str] = None
    serial_number: Optional[str] = None
    inventory_number: Optional[str] = None

    ip_address: Optional[str] = None
    mac_address: Optional[str] = None
    hostname: Optional[str] = None

    comment: Optional[str] = None


class PrinterResponse(PrinterBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

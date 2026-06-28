from pydantic import BaseModel


class DashboardResponse(BaseModel):

    printer_count: int

    cartridge_count: int

    low_stock: int

    repair_count: int

from pydantic import BaseModel, ConfigDict


class StockResponse(BaseModel):

    id: int

    cartridge_id: int

    quantity: int

    minimum_quantity: int

    model_config = ConfigDict(from_attributes=True)

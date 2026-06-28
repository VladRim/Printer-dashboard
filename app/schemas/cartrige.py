from typing import Optional

from pydantic import BaseModel, ConfigDict


class CartridgeBase(BaseModel):

    manufacturer_id: int

    model: str

    color: Optional[str] = None

    resource: Optional[int] = None

    is_original: bool = True


class CartridgeCreate(CartridgeBase):
    pass


class CartridgeUpdate(BaseModel):

    manufacturer_id: Optional[int] = None

    model: Optional[str] = None

    color: Optional[str] = None

    resource: Optional[int] = None

    is_original: Optional[bool] = None


class CartridgeResponse(CartridgeBase):

    id: int

    model_config = ConfigDict(from_attributes=True)

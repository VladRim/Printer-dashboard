from enum import Enum


class StockOperation(str, Enum):

    IN = "IN"

    OUT = "OUT"

    WRITE_OFF = "WRITE_OFF"

    RETURN = "RETURN"

    INVENTORY = "INVENTORY"

from enum import Enum


class PrinterStatus(str, Enum):

    ACTIVE = "ACTIVE"

    REPAIR = "REPAIR"

    OFFLINE = "OFFLINE"

    WRITEOFF = "WRITEOFF"

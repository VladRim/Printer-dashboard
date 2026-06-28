from enum import Enum


class RepairStatus(str, Enum):

    OPEN = "OPEN"

    IN_PROGRESS = "IN_PROGRESS"

    CLOSED = "CLOSED"

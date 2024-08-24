

from enum import Enum


class Status(Enum):
    ACTIVE = 1
    INACTIVE = 0

class StatusOrder(Enum):
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
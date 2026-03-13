from enum import Enum

class BookingAction(Enum):
    APPROVE = "approved"
    COMPLETED = "completed"
    REJECT = "rejected"
    PENDING = "pending"

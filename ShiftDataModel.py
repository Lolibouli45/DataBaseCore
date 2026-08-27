from pydantic import BaseModel

class ShiftCreate(BaseModel):
    timestamp: str
    employee_name: str
    shift_info: str
    shift_project: str
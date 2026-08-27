from fastapi import FastAPI
from DataBaseUtils import DataBase
from ShiftDataModel import ShiftCreate

class Requester:
    def __init__(self):

        self.db = DataBase()
        self.app = FastAPI()

        self.setup_routes()

    def setup_routes(self):

        @self.app.get("/")
        def root():
            return {
                "message": "DataBase Core is running"
            }

        @self.app.get("/employee/id/{employee_id}")
        def get_employee_by_id(employee_id: int):
            payload = self.db.get_employee_by_id(employee_id)
            return {"message": payload}

        @self.app.get("/employee/name/{employee_name}")
        def get_employee_by_name(employee_name: str):
            payload = self.db.get_employee_by_name(employee_name)
            return {"message" : payload}

        @self.app.get("/project/employee/id/{employee_id}")
        def get_project_by_employee_id(employee_id: int):
            payload = self.db.get_project_by_employee_id(employee_id)
            return {"message": payload}

        @self.app.post("/shift")
        def add_shift(shift: ShiftCreate):
            payload = self.db.add_shift(shift.timestamp, shift.employee_name, shift.shift_info, shift.shift_project)
            return {"message": payload}

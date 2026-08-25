from fastapi import FastAPI
from DataBaseUtils import DataBase

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

        @self.app.get("/employee/{employee_id}")
        def get_employee_by_id(employee_id: int):
            payload = self.db.get_employee_by_id(employee_id)
            return {"message": payload}

from app.db.Models import Employee
from app.db.database import session_maker


def get_all_employee():
    with session_maker() as session:
        employee = session.query(Employee).all()
        return employee
def get_employee_by_id(employee_id:int):
    with session_maker() as session:
        employee = session.query(Employee).get(employee_id)
        return employee
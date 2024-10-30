from graphene import ObjectType, String, Int, Field

from app.db.Models import Job, Employee
from app.db.database import session_maker


class JobType(ObjectType):
    id = Int()
    title = String()
    description = String()
    employee_id = Int()
    employee = Field('app.gql.types.EmployeeType.EmployeeType')

    @staticmethod
    def resolve_employee(root, info):
        print(root.id)
        with session_maker() as session:
            print(root.employee_id)
            a = session.query(Employee).filter(Employee.id== root.employee_id).first()
            print (a.id)
            return a

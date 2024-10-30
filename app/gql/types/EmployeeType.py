from graphene import ObjectType, String, Int, List

from app.db.Models import Job
from app.db.database import session_maker
from app.gql.types.JobType import JobType


class EmployeeType(ObjectType):
    id = Int()
    name = String()
    email = String()
    industry = String()
    jobs = List("app.gql.types.JobType.JobType")

    @staticmethod
    def resolve_jobs(root, info):
        print(root.id)
        with session_maker() as session:
            return (session.query(Job).filter(Job.employee_id == root.id).all())
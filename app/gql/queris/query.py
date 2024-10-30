from graphene import List, ObjectType, Int, Field

from app.db.repository.jobs_repository import get_job_by_id, get_all_Jobs
from app.db.repository.employee_repository import get_all_employee, get_employee_by_id
from app.gql.types.EmployeeType import EmployeeType
from app.gql.types.JobType import JobType


class Query(ObjectType):
    employees = List(EmployeeType)
    jobs = List(JobType)
    employee_by_id = Field(EmployeeType, employeeId=Int())
    job_by_id = Field(JobType, jobId=Int())

    @staticmethod
    def resolve_employees(root, info):
        return get_all_employee()

    @staticmethod
    def resolve_employee_by_id(root, info, employeeId):
        return get_employee_by_id(employeeId)

    @staticmethod
    def resolve_jobs(root, info):
        return get_all_Jobs()

    @staticmethod
    def resolve_job_by_id(root, info, jobId):
        return get_job_by_id(jobId)

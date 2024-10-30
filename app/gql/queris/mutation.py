from graphene import ObjectType, Field, Mutation, String, Int, InputObjectType, Boolean
from graphql import GraphQLError
from pyexpat.errors import messages
from returns.result import Failure

from app.db.Models import Job, Employee
from app.db.data import employee_data
from app.db.database import session_maker
from app.gql.types.EmployeeType import EmployeeType
from app.gql.types.JobType import JobType


class JobInput(InputObjectType):
    title = String()
    description = String()
    employee_id = String()


class EmployeeInput(InputObjectType):
    name = String()
    email = String()
    industry = String()


class CreateEmployee(Mutation):
    class Arguments:
        employeeInput = EmployeeInput()

    employee = Field(EmployeeType)

    @staticmethod
    def mutate(root, info,employeeInput):
        new_employee = Employee(**employeeInput)
        with session_maker() as session:
            session.add(new_employee)
            session.commit()
            session.refresh(new_employee)
            return CreateEmployee(employee=new_employee)


class CreateJob(Mutation):
    class Arguments:
        jobInput = JobInput()

    job = Field(JobType)

    @staticmethod
    def mutate(root, info,jobInput):
        with session_maker() as session:
            employee = session.query(Employee).get(jobInput.employee_id)
            new_job = Job(**jobInput)
            session.add(new_job)
            session.commit()
            session.refresh(new_job)
        return CreateJob(job=new_job)


class DeleteEmployee(Mutation):
    class Arguments:
        id = Int()

    success = Boolean()
    message = String()

    @staticmethod
    def mutate(root, info, id):
        with session_maker() as session:
            try:
                to_delete = session.query(Employee).get(id)
                session.delete(to_delete)
                return DeleteEmployee(success=True,message="delete")
            except GraphQLError as e:
                return DeleteEmployee(success=False,message=str(e))


class DeleteJob(Mutation):
    class Arguments:
        id = Int()


    success = Boolean()
    message = String()
    @staticmethod
    def mutate(root, info, id):
        with session_maker() as session:
            try:
                to_delete = session.query(Job).get(id)
                session.delete(to_delete)
                return DeleteJob(success=True, message="delete")
            except GraphQLError as e:
                return DeleteJob(success=False, message=str(e))


class UpdateEmployee(Mutation):
    class Arguments:
        id = Int()
        employeeInput = EmployeeInput()

    employee = Field(EmployeeType)

    @staticmethod
    def mutate(root, info, id, employeeInput):
        with session_maker() as session:
            to_update = session.query(Employee).get(id)
            to_update = session.merge(to_update)
            to_update.name = employeeInput.name
            to_update.industry = employeeInput.industry
            to_update.email = employeeInput.email
            session.commit()
            session.refresh(to_update)
            return UpdateEmployee(employee=to_update)


class UpdateJob(Mutation):
    class Arguments:
        id = Int()
        jobInput = JobInput()

    job = Field(JobType)

    @staticmethod
    def mutate(root, info, id, jobInput):
        with session_maker() as session:
            to_update = session.query(Job).get(id)
            to_update = session.merge(to_update)
            to_update.title = jobInput.title
            to_update.description = jobInput.description
            session.commit()
            session.refresh(to_update)
            return UpdateJob(job=to_update)


class Mutations(ObjectType):
    createEmployee = CreateEmployee.Field()
    createJob = CreateJob.Field()
    deleteEmployee = DeleteEmployee.Field()
    deleteJob = DeleteJob.Field()
    updateEmployee = UpdateEmployee.Field()
    updateJob = UpdateJob.Field()

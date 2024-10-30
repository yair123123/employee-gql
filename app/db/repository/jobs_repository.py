from app.db.Models import Job
from app.db.database import session_maker


def get_all_Jobs():
    with session_maker() as session:
        jobs = session.query(Job).all()
        return jobs
def get_job_by_id(job_id:int):
    with session_maker() as session:
        job = session.query(Job).get(job_id)
        return job

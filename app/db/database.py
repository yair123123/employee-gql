from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.Models import *
from app.db.Models import Base
from app.db.data import employee_data, jobs_data
from app.settings.config import DB_URL

engine =create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)

def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
def fill_table():
    with session_maker() as session:
        all_employees = [Employee(**emp) for emp in employee_data]
        session.add_all(all_employees)
        all_jobs = [Job(**j) for j in jobs_data]
        session.add_all(all_jobs)
        session.commit()
        session.close()
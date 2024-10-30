from sqlalchemy.orm import declarative_base

Base = declarative_base()
from .Job import Job
from .Employee import Employee
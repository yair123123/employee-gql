from sqlalchemy import Column, Integer, String, delete
from sqlalchemy.orm import relationship

from app.db.Models import Base


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False,unique=True)
    industry = Column(String, nullable=False)
    jobs = relationship("Job", back_populates="employee",cascade="all,delete")

from sqlalchemy import Column, Integer, String
from database import Base

class PatientDB(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    age = Column(Integer)
    gender = Column(String)

    phone = Column(String)
    department = Column(String)

    complaint = Column(String)
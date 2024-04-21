from pydantic import BaseModel
from schema.patients import Patient
from schema.doctors import Doctors, Status
from datetime import datetime

class Appointment(BaseModel):
    id: int
    patient: Patient
    doctor: Doctors
    status: str
    appointment_time: datetime
    


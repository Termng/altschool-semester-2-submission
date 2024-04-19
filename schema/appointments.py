# Appointment: id, patient, doctor, date

from pydantic import BaseModel

class appointment(BaseModel):
    id: int
    patient: str
    doctor: int
    date: str
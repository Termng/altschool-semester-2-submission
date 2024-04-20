# Doctors: id, name, specialization, phone, is_available (defaults to True)

from pydantic import BaseModel
from enum import Enum

class Status(str, Enum):
    is_available = "True"
    not_available = "False"

class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: Status = Status.is_available
    
    def set_availability(self, availability: Status):
        self.is_available = availability


    
class DoctorsUpdate(BaseModel):
    name: str
    specialization: str
    phone: str


class DoctorStatus(BaseModel):
    is_available: Status
    
    

doctors: list[Doctors] = [
    Doctors(id=1, name="Falomo", specialization= "Anesthesiology", phone= "+2347037152720", is_available= Status.is_available),
    Doctors(id=2, name="Aderinokun", specialization= "Dermatology", phone= "+2347061703817", is_available= Status.not_available)
]

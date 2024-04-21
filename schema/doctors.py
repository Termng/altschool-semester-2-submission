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
    Doctors(id=1, name="Okafor", specialization="Pediatrics", phone="+2347012345678", is_available=Status.is_available),
    Doctors(id=2, name="Adebayo", specialization="Cardiology", phone="+2348098765432", is_available=Status.is_available),
    Doctors(id=3, name="Eze", specialization="Neurology", phone="+2347087654321", is_available=Status.is_available),
    Doctors(id=4, name="Abubakar", specialization="Orthopedics", phone="+2348123456789", is_available=Status.not_available),
    Doctors(id=5, name="Ogunleye", specialization="Ophthalmology", phone="+2348023456789", is_available=Status.is_available),
    Doctors(id=6, name="Nwosu", specialization="Psychiatry", phone="+2348056789123", is_available=Status.is_available)
]

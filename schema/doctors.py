# Doctors: id, name, specialization, phone, is_available (defaults to True)

from pydantic import BaseModel

class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool = True

doctors: list[Doctors] = [
    Doctors(id=1, name="Falomo", specialization= "Anesthesiology", phone= "+2347037152720", is_available= True),
    Doctors(id=2, name="Aderinokun", specialization= "Dermatology", phone= "+2347061703817", is_available= False)
]

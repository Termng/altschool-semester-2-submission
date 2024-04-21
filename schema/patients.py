from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name:str
    age: int
    sex: str
    weight: int
    height: int
    phone: str
    
    
class PatientUpdate(BaseModel):
    name:str
    age: int
    sex: str
    weight: int
    height: int
    phone: str
    

patient = [
    Patient(id=2, name="Chinedu", age=35, sex="M", weight=70, height=165, phone="+2347012345678"),
    Patient(id=3, name="Chinyere", age=28, sex="F", weight=55, height=160, phone="+2348098765432"),
    Patient(id=4, name="Obinna", age=42, sex="M", weight=80, height=175, phone="+2347087654321"),
    Patient(id=5, name="Ngozi", age=50, sex="F", weight=65, height=170, phone="+2348123456789"),
    Patient(id=6, name="Oluwafemi", age=22, sex="M", weight=60, height=168, phone="+2348023456789"),
    Patient(id=7, name="Olajumoke", age=38, sex="F", weight=70, height=165, phone="+2348056789123")
]

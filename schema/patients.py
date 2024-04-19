# Patient: id, name, age, sex, weight, height, phone
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
    Patient(id=0, name="Ahmed", age=20, sex="M", weight = 50, height=12, phone= "+234782373524" ),
    Patient(id=1, name="Beatrice", age=12, sex="F", weight = 90, height=20, phone= "+234330000000" )
]
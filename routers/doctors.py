from fastapi import APIRouter, Depends,status, HTTPException
from random import randrange
from schema.doctors import Doctors, doctors, DoctorsUpdate, DoctorStatus, Status


doctor_router = APIRouter(
    prefix='/doctor',
    tags=['Doctor']
)


@doctor_router.get("/")
def get_doctors():
    return {"message": doctors}

@doctor_router.get("/{doctor_id}")
def get_one_doctor(doctor_id: int):
    for one in doctors:
        if one.id == doctor_id:
            return one
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "doctor does not exist in database")


@doctor_router.post("/")
def create_doctor(payload: Doctors):
    new_doctor = payload.model_dump()
    new_doctor_id = randrange (2, 999)
    new_doctor["id"] = new_doctor_id
    doctors.append(new_doctor)
    return {"message": "Doctor has been created", "data": new_doctor}

@doctor_router.put("/{doctor_id}")
def update_doctor(doctor_id: int , payload: DoctorsUpdate):
    for person in doctors:
        if person.id == doctor_id:
            person.name = payload.name
            person.specialization = payload.specialization
            person.phone = payload.phone
            return {"successfully updated": person}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Doctor with id = {doctor_id} does not exist")


@doctor_router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int ):
    for person in doctors:
        if person.id == doctor_id:
            doctors.remove(person)
            return {"message": f"the patient with the id {doctor_id} has been deleted"}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'the patient with  id: {doctor_id} does not exist in the database')


@doctor_router.put("/status/{doctor_id}")
def update_availability(doctor_id: int, payload: Status):
    doctor = next((doc for doc in doctors if doc.id == doctor_id), None)
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Doctor with id {doctor_id} not found")

    doctor.set_availability(payload)
    return {"message": f"Doctor with id:{doctor_id} availability updated to {payload}"}
    



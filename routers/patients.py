from fastapi import APIRouter, Depends,status, HTTPException
from random import randrange


from schema.patients import Patient, patient, PatientUpdate

patient_router = APIRouter(
    prefix='/patient',
    tags=['Patient']
)


@patient_router.get("/")
def get_patients():
    return {"message": patient}


@patient_router.get("/{patient_id}")
def get_one_patient(patient_id: int):
    for one in patient:
        if one.id == patient_id:
            return one
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "patient does not exist in database")

@patient_router.post("/")
def create_patient(payload: Patient):
    new_patient = payload.model_dump()
    new_patient_id = randrange (2, 999)
    new_patient["id"] = new_patient_id
    patient.append(new_patient)
    return {"message": "Patient has been created", "data": new_patient}

@patient_router.put("/{patient_id}")
def update_patient(patient_id: int , payload: PatientUpdate):
    for person in patient:
        if person.id == patient_id:
            person.name = payload.name
            person.age = payload.age
            person.sex = payload.sex
            person.weight = payload.weight
            person.height = payload.height
            person.phone = payload.phone
            return  {"message": "Patient has been updated", "Updated data": person}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Patient with id = {patient_id} does not exist")


@patient_router.delete("/{patient_id}")
def delete_patient(patient_id: int):
    for person in patient:
        if person.id == patient_id:
            patient.remove(person)
            return {"message": f"the patient with the id {patient_id} has been deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'the patient with  id: {patient_id} does not exist in the database')
        
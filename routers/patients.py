from fastapi import APIRouter
from schema.patients import Patient, patient, PatientUpdate
from services.patients import PatientService

patient_router = APIRouter(
    prefix='/patient',
    tags=['Patient']
)

@patient_router.get("/")
def get_patients():
    return {"message": patient}


@patient_router.get("/{patient_id}")
def get_patient_by_id(patient_id: int):
    data = PatientService.get_one_patient(patient_id)
    return {'message': 'successful', 'data': data} 


@patient_router.post("/")
def create_patient(payload: Patient):
    data = PatientService.create_patient_resource(payload)
    return {'message': 'successful', 'data': data} 
    
    
@patient_router.put("/{patient_id}")
def update_patient(patient_id: int , payload: PatientUpdate):
    data = PatientService.update_patient_resource(patient_id, payload)
    return {'message': 'successful', 'data': data} 
    

@patient_router.delete("/{patient_id}")
def delete_patient(patient_id: int):
    data = PatientService.create_patient_resource(patient_id)
    return {'message': 'successful', 'data': data} 
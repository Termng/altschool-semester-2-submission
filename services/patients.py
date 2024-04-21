from fastapi import APIRouter,status, HTTPException
from random import randrange
from schema.patients import Patient, patient, PatientUpdate


class PatientService:
    
    @staticmethod
    def get_one_patient(patient_id:int):
        for one in patient:
            if one.id == patient_id:
                return one
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "patient does not exist in database")
    
    @staticmethod
    def create_patient_resource(payload: Patient):
        new_patient = payload.model_dump()
        new_patient_id = randrange (2, 999)
        new_patient["id"] = new_patient_id
        patient.append(new_patient)
        return {"message": "Patient has been created", "data": new_patient}
    
    @staticmethod
    def update_patient_resource(patient_id: int , payload: PatientUpdate):
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
    
    @staticmethod
    def delete_patient_resource(patient_id: int):
        for person in patient:
            if person.id == patient_id:
                patient.remove(person)
                return {"message": f"the patient with the id {patient_id} has been deleted"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'the patient with  id: {patient_id} does not exist in the database')
    
    
    

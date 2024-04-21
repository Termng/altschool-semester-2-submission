from schema.doctors import Doctors, doctors, DoctorsUpdate, Status
from fastapi import HTTPException, status
from random import randrange

class DoctorService:
    
    @staticmethod
    def get_one_doctor(doctor_id: int):
        for one in doctors:
            if one.id == doctor_id:
                return one
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "doctor does not exist in database")
    
    @staticmethod
    def create_doctor_resource(payload: Doctors):
        new_doctor = payload.model_dump()
        new_doctor_id = randrange (2, 999)
        new_doctor["id"] = new_doctor_id
        doctors.append(new_doctor)
        return new_doctor
    
    @staticmethod
    def update_doctor_resource(doctor_id: int , payload: DoctorsUpdate):
        for person in doctors:
            if person.id == doctor_id:
                    person.name = payload.name
                    person.specialization = payload.specialization
                    person.phone = payload.phone
                    return {"successfully updated": person}
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Doctor with id = {doctor_id} does not exist")
    
    @staticmethod
    def delete_doctor_resource(doctor_id: int ):
        for person in doctors:
            if person.id == doctor_id:
                doctors.remove(person)
                return {"message": f"the patient with the id {doctor_id} has been deleted"}
            
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'the Doctor with  id: {doctor_id} does not exist in the database')
    
    
    @staticmethod
    def doctor_status(doctor_id: int, payload: Status):
        doctor = next((doc for doc in doctors if doc.id == doctor_id), None)
        if not doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Doctor with id {doctor_id} not found")

        doctor.set_availability(payload)
        return {"message": f"Doctor with id:{doctor_id} availability updated to {payload}"}
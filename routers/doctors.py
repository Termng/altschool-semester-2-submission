from fastapi import APIRouter
from schema.doctors import Doctors, doctors, DoctorsUpdate, Status
from services.doctors import DoctorService


doctor_router = APIRouter(
    prefix='/doctor',
    tags=['Doctor']
)


@doctor_router.get("/")
def get_doctors():
    return {"message": doctors}


@doctor_router.get("/{doctor_id}")
def get_doctor_by_id(doctor_id: int):
    data = DoctorService.get_one_doctor(doctor_id)
    return {'message': 'successful', 'data': data} 


@doctor_router.post("/")
def create_doctor(payload: Doctors):
    data = DoctorService.create_doctor_resource(payload)
    return {"message": "Doctor has been created", "data": data}


@doctor_router.put("/{doctor_id}")
def update_doctor(doctor_id: int , payload: DoctorsUpdate):
    data = DoctorService.update_doctor_resource(doctor_id, payload)
    return {'message': 'Doctor resource has been updated', 'data': data}


@doctor_router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int ):
    data = DoctorService.delete_doctor_resource(doctor_id)
    return data


@doctor_router.put("/status/{doctor_id}")
def update_availability(doctor_id: int, payload: Status):
    data = DoctorService.doctor_status(doctor_id, payload)
    return data
    



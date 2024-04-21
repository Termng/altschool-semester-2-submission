from fastapi import APIRouter
from services.appointment import AppointmentService, my_appointments

appointment_router = APIRouter(
    prefix='/appointment',
    tags=['Appointment']
)


@appointment_router.post("/")
def create_appointment(patient_id: int):
    data = AppointmentService.create_appointment_resource(patient_id)
    return {"message": "Appointment has been created", "data": data}



@appointment_router.get("/")
def active_appointments():
    return my_appointments



@appointment_router.put("/")
def complete_appointment(appointment_id: int, doctor_id: int):
    data = AppointmentService.complete_appointment_resource(appointment_id, doctor_id)
    return {"message": "Successful", "data": data}
    


@appointment_router.delete("/")
def cancel_appointment(appointment_id: int, doctor_id: int):
    data = AppointmentService.cancel_appointment_resource(appointment_id, doctor_id)
    return {"Successful": data}
    






from fastapi import APIRouter, HTTPException, status
from schema.appointment import Appointment, appointment_data, appointments
from schema.patients import Patient, patient, PatientUpdate
from schema.doctors import Doctors, doctors, DoctorsUpdate, DoctorStatus, Status
from typing import Optional
from datetime import datetime

appointment_router = APIRouter()


def find_available_doctor():
    for doctor in doctors:
        if doctor.is_available == DoctorStatus.is_available:
            return doctor
    return None


@appointment_router.post("/appointments/")
async def create_appointment(patient: Patient, appointment_time: datetime):
    # Find the first available doctor
    doctor = find_available_doctor()
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No available doctors")

    # Create the appointment
    appointment = Appointment(
        id=len(appointments) + 1,  # Generate a unique ID for the appointment
        patient=patient,
        doctor=doctor,
        appointment_time=appointment_time
    )

    # Update doctor status to not available
    doctor.is_available = DoctorStatus.not_available

    # Add the appointment to the list of appointments
    appointments.append(appointment)

    return {"message": "Appointment created successfully", "appointment": appointment}

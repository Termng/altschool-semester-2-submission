from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from schema.patients import Patient, patient
from schema.doctors import Doctors, Status, doctors
from schema.appointment import Appointment
from random import randrange
from datetime import datetime
from utils.doctors import DoctorUtils


my_appointments = []

class AppointmentService:
    
    @staticmethod
    def create_appointment_resource(patient_id: int):
        patients = next((p for p in patient if p.id == patient_id), None)
        if not patients:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")

        
        doctor = DoctorUtils.find_available_doctor()
        if not doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No available doctors")

        
        appointment = Appointment(
            id= randrange(3,200),  
            patient=patients,
            doctor=doctor,
            status= "ongoing",
            appointment_time=datetime.now()  
        )

        # Update doctor status to not available
        doctor.is_available = False

        my_appointments.append(appointment)
        return {"patient_id": patients.id,  "patient_name": patients.name, "doctor_name": doctor.name, "status": appointment.status, "scheduled_time": datetime.now().isoformat()}
    
    
    @staticmethod
    def complete_appointment_resource(appointment_id: int, doctor_id: int):
        authorized_doctors_ids = [doctor.id for doctor in doctors]
        if doctor_id not in authorized_doctors_ids:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Only doctors can complete appointments")

        
        appointment = None
        for app in my_appointments:
            if app.id == appointment_id:
                appointment = app
                break
        
        if appointment is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Appointment with id {appointment_id} not found")

        my_appointments.remove(appointment)

        return {"message": f"Appointment with id: {appointment_id} has been set to complete"}
    
    
    @staticmethod
    def cancel_appointment_resource(appointment_id: int, doctor_id: int):
        # Find the doctor by ID
        doctor = next((doc for doc in doctors if doc.id == doctor_id), None)
        if not doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Doctor with id {doctor_id} not found")

        
        if not doctor.is_available:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Only available doctors can cancel appointments")

        
        appointment = None
        for app in my_appointments:
            if app.id == appointment_id:
                appointment = app
                break
        
        if appointment:
            appointment.doctor.is_available = True
            my_appointments.remove(appointment)
            
            return {"message": "Appointment canceled successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Appointment with id {appointment_id} not found")
        
        
        
        
        



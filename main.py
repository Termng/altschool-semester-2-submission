from fastapi import FastAPI
from routers.patients import patient_router
from routers.doctors import doctor_router
from routers.appointment import appointment_router


app = FastAPI(
    docs_url='/'
    
)

app.include_router(patient_router)
app.include_router(doctor_router)
app.include_router(appointment_router)

@app.get('/welcome')
def index():
    return {'message': 'This is Torahs application'}
from fastapi import FastAPI
from routers.patients import patient_router

app = FastAPI(
    docs_url='/'
    
)

app.include_router(patient_router)

@app.get('/welcome')
def index():
    return {'message': 'This is Torahs application'}
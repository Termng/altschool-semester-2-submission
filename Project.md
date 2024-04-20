The API should provide the following endpoints:

1. CRUD endpoints for Patients

2. CRUD endpoints for Doctors

3. Create an appointment. Only patients can create an appointment. When a patient tries to create an appointment, the first available doctor is assigned to the Appointment. If no doctors are available, return the appropriate response and status code to the user.

4. Complete an appointment. Doing this will make the Doctor available again and other patients can book the doctor.

5. Cancel an appointment before it is completed, making the doctor free again.

6. Set availability status. This is for the Doctors, allowing them to set their status to unavailable to prevent them from being booked.


NOTE:

For your database, use an in-memory data structure such as list or dictionaries.
Use Pydantic for data validation.
Use the appropriate status codes where necessary.
Use proper code structuring.
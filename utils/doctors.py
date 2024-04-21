from schema.doctors import doctors


class DoctorUtils:
    @staticmethod
    def find_available_doctor():
        for doctor in doctors:
            if doctor.is_available:
                return doctor
        return None
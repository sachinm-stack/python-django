class Person:

    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact

    def introduce(self):
        print(f"Name: {self.name} | Age: {self.age} | Contact: {self.contact}")


class Patient(Person):

    def __init__(self, name, age, contact):
        super().__init__(name, age, contact)
        self.__medical_record = ""   # private

    def get_record(self, authorised_by):
        if authorised_by in ['doctor', 'nurse']:
            return self.__medical_record
        return "Access denied!"

    def update_record(self, record, authorised_by):
        if authorised_by in ['doctor', 'nurse']:
            self.__medical_record = record
            print("Medical record updated.")
        else:
            print("Access denied!")


class Doctor(Person):

    def __init__(self, name, age, contact, specialisation):
        super().__init__(name, age, contact)
        self.specialisation = specialisation
        self.patients = []

    def add_patient(self, patient):
        if not isinstance(patient, Patient):
            print("Invalid patient!")
            return
        self.patients.append(patient)
        print(f"{patient.name} added to Dr. {self.name}'s list")

    @classmethod
    def create_specialist(cls, name, age, contact, specialisation):
        return cls(name, age, contact, specialisation)

    @staticmethod
    def is_available(shift):
        return shift.lower() in ['morning', 'afternoon']


class Hospital:
    total_hospitals = 0

    def __init__(self, name):
        self.name = name
        self.doctors = []
        Hospital.total_hospitals += 1

    def add_doctor(self, doctor):
        if not isinstance(doctor, Doctor):
            print("Invalid doctor!")
            return
        self.doctors.append(doctor)
        print(f"Dr. {doctor.name} added to {self.name}")

    def find_doctor(self, specialisation):
        for doc in self.doctors:
            if doc.specialisation.lower() == specialisation.lower():
                print(f"Found: Dr. {doc.name} ({doc.specialisation})")
                return
        print("No doctor found!")


# ---------------- DEMO ----------------

# Create hospital
h1 = Hospital("City Hospital")

# Create doctor using class method
d1 = Doctor.create_specialist("Ravi", 45, "9999999999", "Cardiology")

# Create patient
p1 = Patient("Rahul", 30, "8888888888")

# Add doctor to hospital
h1.add_doctor(d1)

# Add patient to doctor
d1.add_patient(p1)

# Introduce
p1.introduce()
d1.introduce()

# Update medical record
p1.update_record("Heart condition stable", "doctor")

# Access medical record
print(p1.get_record("doctor"))   # allowed
print(p1.get_record("visitor"))  # denied

# Find doctor
h1.find_doctor("cardiology")

# Check availability
print(Doctor.is_available("morning"))   # True
print(Doctor.is_available("night"))     # False

# Total hospitals
print("Total hospitals:", Hospital.total_hospitals)
class Patient:
    __name : str
    __bill_amount : float
    def __init__(self, name, bill_amount, ):
        self.__name = name
        self.__bill_amount = bill_amount
        self.__ptype = type
        
    def get_name(self):
        return self.__name
        
    def get_bill_amount(self):
        return self.__bill_amount
        
    def set_name(self, name):
        self.__name = name
        
    def set_bill_amount(self, bill_amount):
        if bill_amount > 0:
            self.__bill_amount = bill_amount
            
    def calculate_bill(self):
        return self.__bill_amount
        
    def display_patient_type(self):
        return "Regular Patient"

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80
        
    def display_patient_type(self):
        return "Senior Patient"
        
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85
        
    def display_patient_type(self):
        return "PhilHealth Patient"
        
patients = []

def add_patients(patient):
    patients.append(patient)
    
def display_bill(patient):
    print(f"Patient Name: {patient.get_name()}")
    print(f"Patient Type: {patient.display_patient_type()}")
    print(f"Original Bill: P{patient.get_bill_amount()}")
    print(f"Final Bill: P{patient.calculate_bill()}")
    
add_patients(Patient("Juan Dela Cruz", 15000))
add_patients(SeniorPatient("Maria Santos", 15000))
add_patients(PhilHealthPatient("Pedro Reyes", 15000))
    
print("Hospital Billing System")
print("-" * 23)

for patient in patients:
    display_bill(patient)
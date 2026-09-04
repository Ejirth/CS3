class Lab:
    def __init__(self, room_number):
        self.room_number = room_number

class Technician:
    def __init__(self, name, assigned_lab=None):
        self.name = name
        self.assigned_lab = assigned_lab

    def assign_lab(self, lab_obj):
        self.assigned_lab = lab_obj
        
room_num = input("Enter the laboratory room number: ")
chem_lab = Lab(room_num)
mr_cruz = Technician("Mr. Cruz")

mr_cruz.assign_lab(chem_lab)

print("Technician:", mr_cruz.name)
print("Assigned Room:", mr_cruz.assigned_lab.room_number)
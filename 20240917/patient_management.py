# 1.    class Patient {id ,name} ----------------------------------------

class Patient:
    def __init__(self,id, name):
        self.id = id
        self.name = name
        
    def __str__(self):
        return f'[id={self.id}, name={self.name}]'
    
    def __repr__(self) -> str:
        pass


# 2.    patient []

patients = []

# 3.    patient_add (id, name) ------------------------------------------

def patient_add (id,name):
    global patients
    patient = Patient(id, name)
    patients.append(patient)

# 4.    patient_remove (id) ---------------------------------------------

def patient_remove (id):
    global patients
    for patient in patients:
        if patient.id ==id:
            print(patient)
            if input ('Are you sure to delete (Yes/No)?').lower == 'Yes':
                patients.remove(patient)
                print('Patient deleted successfully.')
            return
    print(f'No such id {id}')

# 5.    patient_display () ----------------------------------------------

def patient_display():
    global patients
    for patient in patients:
        print(patient)
        
# 6.    patient_update () -----------------------------------------------

def patient_update_by_id ():
    global patients
    for patient in patients:
        if patient.id ==id:

# 7.    menu ------------------------------------------------------------

def menu():
    choice = int(input('''1- Add Patient
2- Remove Patient
3- Display Patient by id
4- Display all Patient
5- Update by id
7- Terminate                   
your choice: '''))
    if choice == 1:
        id = int(input('Enter patient id: '))
        name = input('Enter patient name: ')
        patient_add(id, name)
    elif choice == 2:
        id = int(input('Enter patient id to discharge: '))
        patient_remove(id)
    elif choice == 3:
        patient_display(id)
    elif choice == 4:
        patient_display()
    elif choice == 5:
        patient_update_by_id(id) 
    elif choice == 7:
        pass 
    else:
        print('Invalid Option-----')
    return

# 7.    menus() --------------------------------------------------------

def menus():
    choice = menu()
    while choice != 7:
        choice = menu()
    print('------- Thank you! For using our Healthcare Facilities. -----------')

# 8.    driver program -------------------------------------------------

menus()


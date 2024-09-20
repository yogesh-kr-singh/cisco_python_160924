from patient import Patient


# 2.    patient {}

patients = {} #dict()

# 3.    patient_add (id, name) ------------------------------------------

def patient_add (id,name):
    global patients
    patient = Patient(id, name)
    patients[patient.id]= patient #patients.append(patient)
    print('Patient data created successfully.--------')

# 4.    patient_remove (id) ---------------------------------------------

def patient_remove (id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'------- No - such - id - to - be - found ------- {id}')
        return
    print(patient)
    if input ('Are you sure to delete (yes/no)?').lower() == 'yes':
        del patients[id] # patients.remove(patient)
        print('Patient data deleted successfully.--------')
    
# 5.    patient_display_by_id () ----------------------------------------

def patient_display_by_id(id):
    global patients
    patient = patients.get(id) #for id in patients:
    print(patients[id])
    if patient == None: #print(patients[id]) 
        print(f'------- No - such - id - to - be - found ------- {id}')
        return
        
# 6.    patient_display () ----------------------------------------------

def patient_display():
    global patients
    if len(patients)==0:
        print('- - - - Empty Data (404 Error) - - - -')
        return
    for id in patients: #for patient in patients:
        print(patients[id]) #print(patient)
    
    
        
# 7.    patient_update () -----------------------------------------------

def patient_update_by_id (id):
    global patients
    patient = patients.get(id) #for patient in patients:
    if patient == None: #if patient.id ==id:
        print(f'------- No - such - id - to - be - found ------- {id}')
        return
    print(patient)
    name = input (f'Enter the updated name: ({patient.name})')
    patient.name = name
    print('Patient data updated successfully.-------')
    
            
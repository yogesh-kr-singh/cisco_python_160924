from patient_service import patient_add, patient_remove, patient_display_by_id, patient_display, patient_update_by_id

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
        id = int(input('Enter patient id to display: '))
        patient_display_by_id(id)
    elif choice == 4:
        patient_display()
    elif choice == 5:
        id = int(input('Enter patient id to upadte: '))
        patient_update_by_id(id) 
    elif choice == 7:
        pass 
    else:
        print('- - - - Invalid Option - - - -')
    return choice

# 7.    menus() --------------------------------------------------------

def menus():
    choice = menu()
    while choice != 7:
        choice = menu()
    print('------- | Thank you! For using our Healthcare Facilities. | -----------')

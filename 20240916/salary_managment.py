salaries = []

def salary_add(salary):
    global salaries 
    salaries.append(salary) 

def salary_delete(salary):
    global salaries 
    try:
        salaries.remove(salary)
    except ValueError as err:
        print('No such salary')

def salary_sum():
    global salaries 
    s = 0 
    for salary in salaries:
        s += salary 
    return s

def salary_avg():
    global salaries 
    if len(salaries) == 0:
        return 0
    s = sum(salaries)
    count = len(salaries)
    avg = s / count 
    return avg  

def salary_max():
    global salaries
    return max(salaries)

def salary_min():
    global salaries
    return min(salaries)

def menu():
    try:
        choice = int(input('''1-add
2-delete
3-sum
4-avg
5-min
6-max
7-end                       
your choice: '''))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        return None

    if choice == 1:
        salary = float(input('Enter salary: '))
        salary_add(salary)
        print(salaries)
    elif choice == 2:
        salary = float(input('Enter salary: '))
        salary_delete(salary)
        print(salaries)
    elif choice == 3:
        s = salary_sum()
        print(s)
    elif choice == 4:
        avg = salary_avg()
        print(avg)
    elif choice == 5:
        min_salary = salary_min()
        print(min_salary)
    elif choice == 6:
        max_salary = salary_max()
        print(max_salary)
    elif choice == 7:
        return choice
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
    return choice

def menus():
    choice = menu()
    while choice != 7:
        if choice is not None:
            choice = menu()
    print('App Ended')

menus()

import pickle
import os

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

def menu():
    print("Employee Management System")
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change employee information")
    print("4. Delete an employee")
    print("5. Quit")

def save_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    else:
        return {}

def add_employee(employee_dict):
    name = input("Enter employee name: ")
    id_number = int(input("Enter employee ID number: "))
    department = input("Enter employee department: ")
    job_title = input("Enter employee job title: ")
    new_employee = Employee(name, id_number, department, job_title)
    employee_dict[id_number] = new_employee
    print("Employee added.")

def change_employee(employee_dict, employee_id):
    if employee_id in employee_dict:
        employee = employee_dict[employee_id]
        print("Changing information for:", employee.name)
        employee.name = input("Enter new name: ")
        employee.department = input("Enter new department: ")
        employee.job_title = input("Enter new job title: ")
        print("Employee information updated.")
    else:
        print("Employee not found.")

def delete_employee(employee_dict, employee_id):
    if employee_id in employee_dict:
        del employee_dict[employee_id]
        print("Employee deleted.")
    else:
        print("Employee not found.")

def lookup_employee(employee_dict, employee_id):
    if employee_id in employee_dict:
        employee = employee_dict[employee_id]
        print("Employee Found:")
        print("Name:", employee.name)
        print("ID Number:", employee.id_number)
        print("Department:", employee.department)
        print("Job Title:", employee.job_title)
    else:
        print("Employee not found.")

if __name__ == "__main__":
    data_filename = "employee_data.pkl"
    employee_data = load_data(data_filename)
    while True:
        menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            employee_id = int(input("Enter employee ID to look up: "))
            lookup_employee(employee_data, employee_id)
        elif choice == '2':
            add_employee(employee_data)
        elif choice == '3':
            employee_id = int(input("Enter employee ID to modify: "))
            change_employee(employee_data, employee_id)
        elif choice == '4':
            employee_id = int(input("Enter employee ID to delete: "))
            delete_employee(employee_data, employee_id)
        elif choice == '5':
            save_data(employee_data, data_filename)
            print("Quitting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

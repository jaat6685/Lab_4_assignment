class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def _init_(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, target_age):
        matching_employees = [emp for emp in self.employees if emp.age == target_age]
        return matching_employees

    def search_by_name(self, target_name):
        matching_employees = [emp for emp in self.employees if emp.name == target_name]
        return matching_employees

    def search_by_salary(self, operator, target_salary):
        operators = {
            ">": lambda x, y: x > y,
            "<": lambda x, y: x < y,
            ">=": lambda x, y: x >= y,
            "<=": lambda x, y: x <= y,
        }
        if operator not in operators:
            raise ValueError("Invalid operator")
        matching_employees = [emp for emp in self.employees if operators[operator](emp.salary, target_salary)]
        return matching_employees

def main():
    emp_db = EmployeeDatabase()

    # Populate the employee database
    emp_db.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Ujjwal Kharkwal, E22CSEU1108")
    print("Choose a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        target_age = int(input("Enter the age to search for: "))
        result = emp_db.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter the name to search for: ")
        result = emp_db.search_by_name(target_name)
    elif choice == 3:
        operator = input("Enter the operator (>, <, <=, >=): ")
        target_salary = int(input("Enter the salary to search for: "))
        result = emp_db.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice")
        return

    if not result:
        print("No matching employees found.")
    else:
        print("Matching Employees:")
        for emp in result:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    main()

##  https://www.w3resource.com/python-exercises/class-exercises/python-class-real-life-problem-1.php

class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.id = emp_id
        self.salary = salary
        self.department = department

    def calculate_salary(self, salary, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.salary = self.salary + (overtime * (self.salary / 50))

    def assign_department(self, emp_department):
        self.department = emp_department

    def print_employee_details(self):
        print("\nName: ", self.name)
        print("ID: ", self.id)
        print("Salary: ", self.salary)
        print("Department: ", self.department)
        print("----------------------")


employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")
employee5 = Employee("AME", "E7699", 32100, "ACCOUNTING")

print("Original Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()
employee5.print_employee_details()

employee1.assign_department("OPERATIONS")
employee4.assign_department("SALES")
employee5.assign_department("RESEARCH")

employee2.calculate_salary(45000, 52)
employee4.calculate_salary(45000, 60)
employee5.calculate_salary(32100, 65)

print("Updated Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()
employee5.print_employee_details()
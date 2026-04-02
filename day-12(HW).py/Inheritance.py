class Employee:

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print(f"Employee: {self.name} | ID: {self.emp_id} | Salary: ₹{self.salary}")

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name}'s new salary: ₹{self.salary}")


class Manager(Employee):

    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department
        self.team = []

    def add_to_team(self, employee):
        if not isinstance(employee, Employee):
            print("Invalid employee!")
            return
        self.team.append(employee)

    def display(self):   # method override
        super().display()
        print(f"Department: {self.department} | Team size: {len(self.team)}")


# Demo
e1 = Employee('Rahul', 'E001', 50000)
e2 = Employee('Anita', 'E002', 55000)

m1 = Manager('Ravi', 'M001', 120000, 'Engineering')

m1.add_to_team(e1)
m1.add_to_team(e2)

e1.display()
m1.display()
m1.give_raise(10000)
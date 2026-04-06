class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def display(self):
        print(f'Name: {self.name} | Age: {self.age}')


class Employee(Person):
    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age)
        self.emp_id     = emp_id
        self.department = department

    def display(self):
        super().display()
        print(f'ID: {self.emp_id} | Dept: {self.department}')


class Manager(Employee):
    def __init__(self, name, age, emp_id, department, team_size):
        super().__init__(name, age, emp_id, department)
        self.team_size = team_size

    def display(self):
        super().display()
        print(f'Team size: {self.team_size}')


# Test
m = Manager('Ravi', 35, 'M001', 'Engineering', 8)
m.display()
# 11.3
print("\n11.3")


class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_salary=5000):
        self.salary += raise_salary
        print(f"{self.first_name} {self.last_name} zarabia teraz: {self.salary}zl")

class Robot():
    def __init__(self):
        self._protectedfield = '1'
        self.__privatefield = '2'

    def _protectedmethod(self):
        print('Protected')

    def __privatemethod(self):
        print('Private')


robot = Robot()
print(robot.__dir__())

print(robot._protectedfield)
# print(robot.__privatefield)
print(robot._Robot__privatefield)

print(robot._protectedmethod())
print(robot._Robot__privatemethod())

print(f"\n ### RESISTOR")


class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


r1 = Resistor(50e3)
print(r1.ohms)
r1.ohms = 10e3
print(r1.ohms)
r1.ohms += 5e3
print(r1.ohms)


class FixedResistor(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms

r2 = FixedResistor(1e3)
print(r2.ohms)
r2.ohms = 2e3
print(r2.ohms)

print(f"\n ### HOMEWORK")

class Homework:
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Ocena musi byc w zakresie 0 - 100")
        self._grade = value


h1 = Homework()
h1.grade = 95
print(h1.grade)


class Employee:
    company = "OpenAI"

    def __init__(self, name, salary, bonus):

        self.name = name

        self._salary = salary

        self.__bonus = bonus

    def show_details(self):

        print("Company: ", Employee.company)
        print("Name: ", self.name)
        print("salary: ", self._salary)
        print("Bonus: ", self.__bonus)

e1 = Employee("Lisha", 50000, 10000)

e1.show_details()
class Employee:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def get_info(self):
        return (f"Сотрудник: Имя - {self.name}, id - {self.id}")


class Manager(Employee):
    def __init__(self, name: str, id: int, department: str):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self):
        return f"{self.name} управляет проектами в отделе {self.department}."


class Technician(Employee):
    def __init__(self, name: str, id: int, specialization: str):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} выполняет обслуживание в области {self.specialization}."


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.list_employee = []

    def get_info(self):
        return (f"Тех-мен {self.name}, id - {self.id}, департамент {self.department},\
специализация {self.specialization}, его команда:")

    def add_employee(self, employee):
        self.list_employee.append(employee)

    def get_team_info(self):
        return ("\n".join(self.list_employee))


employee1 = Employee("Максим", 101)
employee2 = Technician("Ваня", 103, "электроника")
manager = Manager("Данил", 102, "ИТтт")
tech_manager = TechManager("Женя", 104, "ИТ", "разработка ПО")

tech_manager.add_employee(employee1.get_info())
tech_manager.add_employee(employee2.get_info())
tech_manager.add_employee(manager.get_info())

print(tech_manager.get_info())
print(tech_manager.get_team_info())
print(employee2.perform_maintenance())
print(manager.manage_project())
print(tech_manager.perform_maintenance())
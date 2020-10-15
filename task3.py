class Worker:

    name = None

    surname = None

    position = None

    _income = {
        'wage': 'wage',
        'bonus': 'bonus'
    }


class Position(Worker):

    def __init__(self, name:str, surname:str, wage:float, bonus:float):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position = Position(name="Vanya", surname="Petrovich", wage=15.23, bonus=10.33)

print(position.get_full_name())
print(position.get_total_income())
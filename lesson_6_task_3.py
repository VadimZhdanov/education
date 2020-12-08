class Worker:
    def __init__(self, worker_name, worker_surname, worker_pisition, worker_wage, worker_bonus):
        self.name = worker_name
        self.surname = worker_surname
        self.position = worker_pisition
        self._income = {'wage': worker_wage, 'bonus': worker_bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'Имя - {self.name}, Фамилия - {self.surname}')
    def get_total_income(self):
        total_income = self._income.get('wage') + self._income.get('bonus')
        print(f'Итоговая зарплата - {total_income}')

new_worker = Position('Ivan', 'Ivanov', 'CEO', 15000, 3000)
new_worker.get_full_name()
new_worker.get_total_income()






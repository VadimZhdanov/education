class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationary):
    def draw(self):
        return 'Запуск отрисовки ручкой'


class Pencil(Stationary):
    def draw(self):
        return 'Запуск отрисовки карандашом'


class Handle(Stationary):
    def draw(self):
        return 'Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
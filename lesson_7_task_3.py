class Cell:
     def __init__(self, parts):
         self.parts = parts

     def make_order(self, rows):
         row = ''
         for i in range(int(self.parts) // rows):
             row += f'{"*" * rows} \\n'
         row += f'{"*" * (self.parts % rows)}'
         return row


     def __str__(self):
         return str(self.parts)

     def __add__(self, other):
         return f'Сложение клеток {(self.parts + other.parts)}'

     def __sub__(self, other):
         return 'Разность клеток ' + str(self.parts - other.parts) if self.parts - other.parts > 0 \
             else 'Вычитание невозможно'

     def __mul__(self, other):
         return 'Умножение клеток ' + str(self.parts * other.parts)

     def __truediv__(self, other):
         return 'Деление клеток ' + str(round(self.parts / other.parts))


cell_1 = Cell(20)
cell_2 = Cell(11)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1 + cell_2)
print(cell_1.make_order(4))
print(cell_2.make_order(3))
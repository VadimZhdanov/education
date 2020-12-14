class Matrix:
     def __init__(self, matrix_info):
         self.info = matrix_info

     def __str__(self):
         return '\n'.join([' '.join([str(el) for el in line]) for line in self.info])

     def __add__(self, other):
         final_result = ''
         if len(self.info) == len(other.info):
             for line_1, line_2 in zip(self.info, other.info):
                 if len(line_1) != len(line_2):
                     return 'Размеры матриц не соответствуют друг другу!'

                 summ_line = [x + y for x, y in zip(line_1, line_2)]
                 final_result += ' '.join([str(i) for i in summ_line]) + '\n'
         else:
             return 'Размеры матриц не соответствуют друг другу!'
         return final_result

matrix_1 = Matrix([[1, 2], [3, 4]])
matrix_2 = Matrix([[4, 3], [2, 1]])
print(matrix_1 + matrix_2)



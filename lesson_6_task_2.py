class Road:
    def __init__(self, var_1, var_2):
        self._length = int(var_1)
        self._width = int(var_2)
    def mass_count(self):
        mass_for_one_square_metre = int(15)
        thickness = int(4)
        mass = self._width * self._length * mass_for_one_square_metre * thickness
        print(f'Масса асфальта: {mass}')

my_road = Road(1000, 10)
my_road.mass_count()


from time import sleep

class TrafficLight:
    __color = ['red', 'yellow', 'green']
    def runnig(self):
        print('Включение светофора...')
        i = 0
        while i <= 2:
            print(f'Загорелся {TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(8)
            else:
                break
            i += 1

my_traffic_light = TrafficLight()
my_traffic_light.runnig()



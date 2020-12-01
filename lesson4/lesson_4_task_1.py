from sys import argv
name, work_time, salary, bonus_salary = argv
try:
    work_time = int(work_time)
    salary = int(salary)
    bonus_salary = int(bonus_salary)
#    name = argv[0]
#    work_time = int(argv[1])
#    salary = int(argv[2])
#    bonus_salary = int(argv[3])
    my_result = work_time * salary + bonus_salary
    print(name)
    print(f'Результат: {my_result}')
except ValueError:
    print('Ошибка при вводе данных')
# Не понимаю в чем ошибка, с виду все совпадает с примерами из вебинара и методички, но когда запускаю через командную
# строку, указывая нужное количество параметров, всегда пишет, что указан лишь один параметр из ожидаемых четырех
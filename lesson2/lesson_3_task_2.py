def my_func(name, surname, age, city, mail, tel):
    print(f'Имя: {name}; Фамилия: {surname}; Возраст: {age}; Город: {city}; Почта: {mail}; Телефон: {tel}')
my_func(name=input('Введите имя:'), surname=input('Введите фамилию:'),
        age=int(input('Введите возраст:')), city=input('Введите город проживания'),
        mail=input('Укажите почту:'), tel=input('Укажите номер телефона:'))

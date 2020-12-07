with open('file3.txt', 'r') as my_obj:
    avg_sal = []
    low_sal = []
    worker_list = my_obj.readlines()
    for worker in worker_list:
        worker = worker.split()
        avg_sal.append(worker[1])
        if float(worker[1]) < 20000:
            low_sal.append(worker[0])
    avg = sum(map(float, avg_sal)) / len(avg_sal)
print(f'ЗП меньше 20000 у следующих сотрудников: {low_sal}, средняя ЗП: {avg}')


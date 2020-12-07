import json
my_dict = {}
average_profit = []
with open('file7.txt') as my_obj:
    data = my_obj.readlines()
for line in data:
    name, form, revenue, costs = line.split()
    profit = int(revenue) - int(costs)
    my_dict[name] = profit
    if profit > 0:
        average_profit.append(profit)
average_profit = sum(average_profit) / len(average_profit)
info_for_json = [my_dict, {'average_profit': average_profit}]
with open('file7.json', 'w') as my_json:
    json.dump(info_for_json, my_json)
with open('7.json') as f_json:
    print(json.load(f_json))
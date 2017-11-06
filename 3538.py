days = ["shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"]
day_dict = {day:True for day in days}

for i in range(3):
    input()
    for day in input().split():
        day_dict[day] = False
print(sum(day_dict[day] for day in day_dict))

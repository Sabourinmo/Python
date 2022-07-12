import random

employee = ["Paul", "Mike", "Karen", "Brent", "Lisa"]
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
shift =["AM", "PM", "Night"]

week_schedule = {}
for day in week:
    available_employee = []
    for item in employee:
        available_employee.append(item)

    day_schedule ={}
    for x in shift:
        random_employee = random.choice(available_employee)
        available_employee.remove(random_employee)
        day_schedule.update({x:random_employee})
    
    week_schedule.update({day:day_schedule})

print(week_schedule)
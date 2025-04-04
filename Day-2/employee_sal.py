employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]
updated_salaries= list(map(
    lambda employee:{
        **employee,
        "salary":employee["salary"] * 1.1 if employee["rating"]>= 4 else
        employee["salary"]*1.05 if employee["rating"]>=3 and employee["rating"]<4
        else employee["salary"]*0.97 
    },employees
))

print(updated_salaries)
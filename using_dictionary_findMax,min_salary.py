data={
    'John':25000,
    'Jimmy': 45000,
    'Joe': 55500,
    'Tomm Hardy': 70000,
    'Tom Cruise': 80000,
    'Christian Belle': 95000}
max_salary=float('-inf')
min_salary=float('inf')
max_name=''
min_name=''
for name,salary in data.items():
    if(salary > max_salary):
        max_salary=salary
        max_name=name
    if(salary < min_salary):
        min_salary=salary
        min_name=name
print(f"{max_name} got the highest salary  {max_salary}")            
print(f"{min_name} got the lowest salary  {min_salary}")            
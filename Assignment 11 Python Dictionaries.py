# Dictionaries practice (Q31-Q40)

print("Q31")
student = {"name": "Ali", "age": 22, "course": "Python", "marks": 85}
print(student["name"])
print(student["marks"])
print(student.get("city", "Karachi"))

print("Q32")
employee = {"name": "Sara", "salary": 100000, "department": "IT"}
employee["salary"] = employee["salary"] * 1.20
employee["bonus"] = 15000
employee["department"] = "Data Engineering"
print(employee)

print("Q33")
product = {"id": 101, "name": "Laptop", "price": 120000, "stock": 5}
print(product.keys())
print(product.values())
print(product.items())
stock = product.pop("stock")
print(stock)
print(product)

print("Q34")
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 50, "d": 40}
merged = dict1 | dict2
print(merged)

print("Q35")
marks = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Zain": 88}
print(max(marks.values()))
print(min(marks.values()))
print(sum(marks.values()) / len(marks))
print(max(marks, key=marks.get))

print("Q36")
employees = {
    "E101": {"name": "Ali", "salary": 80000},
    "E102": {"name": "Sara", "salary": 120000},
    "E103": {"name": "Ahmed", "salary": 95000}
}
print(employees["E102"]["salary"])
employees["E101"]["salary"] = employees["E101"]["salary"] * 1.15
payroll = employees["E101"]["salary"] + employees["E102"]["salary"] + employees["E103"]["salary"]
print(employees["E101"]["salary"])
print(payroll)

print("Q37")
data = {"Python": "Ali", "SQL": "Sara", "AWS": "Ahmed"}
inverse = dict(zip(data.values(), data.keys()))
print(inverse)

print("Q38")
order = {
    "laptop": {"price": 120000, "quantity": 2},
    "mouse": {"price": 1500, "quantity": 5},
    "keyboard": {"price": 3500, "quantity": 3}
}
laptop_total = order["laptop"]["price"] * order["laptop"]["quantity"]
mouse_total = order["mouse"]["price"] * order["mouse"]["quantity"]
keyboard_total = order["keyboard"]["price"] * order["keyboard"]["quantity"]
grand_total = laptop_total + mouse_total + keyboard_total
print(laptop_total, mouse_total, keyboard_total)
print(grand_total)
print(grand_total * 0.90)

print("Q39")
employees = {
    "Ali": {"python": 90, "sql": 85, "aws": 88},
    "Sara": {"python": 95, "sql": 92, "aws": 90},
    "Ahmed": {"python": 80, "sql": 87, "aws": 84}
}
averages = {
    "Ali": sum(employees["Ali"].values()) / len(employees["Ali"]),
    "Sara": sum(employees["Sara"].values()) / len(employees["Sara"]),
    "Ahmed": sum(employees["Ahmed"].values()) / len(employees["Ahmed"])
}
print(averages)
print(max(averages, key=averages.get))
print(max(employees["Ali"]["sql"], employees["Sara"]["sql"], employees["Ahmed"]["sql"]))

print("Q40")
inventory = {
    "P101": {"name": "Laptop", "price": 120000, "stock": 5},
    "P102": {"name": "Mouse", "price": 1500, "stock": 20},
    "P103": {"name": "Keyboard", "price": 3500, "stock": 10}
}
total_value = (
    inventory["P101"]["price"] * inventory["P101"]["stock"]
    + inventory["P102"]["price"] * inventory["P102"]["stock"]
    + inventory["P103"]["price"] * inventory["P103"]["stock"]
)
values = {
    "P101": inventory["P101"]["price"] * inventory["P101"]["stock"],
    "P102": inventory["P102"]["price"] * inventory["P102"]["stock"],
    "P103": inventory["P103"]["price"] * inventory["P103"]["stock"]
}
print(total_value)
print(inventory[max(values, key=values.get)]["name"])
inventory["P101"]["stock"] -= 2
inventory["P102"]["stock"] -= 5
print(inventory)

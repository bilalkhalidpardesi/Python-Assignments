# Mixed data structures practice (Q41-Q50)

print("Q41")
students = [
    {"id": 1, "name": "Ali", "marks": (85, 90, 88)},
    {"id": 2, "name": "Sara", "marks": (92, 95, 91)},
    {"id": 3, "name": "Ahmed", "marks": (78, 84, 80)}
]
averages = {
    students[0]["name"]: sum(students[0]["marks"]) / len(students[0]["marks"]),
    students[1]["name"]: sum(students[1]["marks"]) / len(students[1]["marks"]),
    students[2]["name"]: sum(students[2]["marks"]) / len(students[2]["marks"])
}
print(averages)
print(max(averages, key=averages.get))
print((students[0]["name"], students[1]["name"], students[2]["name"]))
print(set(students[0]["marks"]) | set(students[1]["marks"]) | set(students[2]["marks"]))

print("Q42")
employees = {
    "Ali": {"Python", "SQL", "AWS"},
    "Sara": {"Python", "Databricks", "SQL"},
    "Ahmed": {"AWS", "Snowflake", "SQL"}
}
print(employees["Ali"] & employees["Sara"] & employees["Ahmed"])
print(employees["Ali"] - employees["Sara"] - employees["Ahmed"])
print(employees["Ali"] | employees["Sara"] | employees["Ahmed"])
python_sql = set()
if {"Python", "SQL"}.issubset(employees["Ali"]):
    python_sql.add("Ali")
if {"Python", "SQL"}.issubset(employees["Sara"]):
    python_sql.add("Sara")
if {"Python", "SQL"}.issubset(employees["Ahmed"]):
    python_sql.add("Ahmed")
print(python_sql)

print("Q43")
sales = [
    ("Laptop", 120000, 2),
    ("Mouse", 1500, 5),
    ("Keyboard", 3500, 3)
]
revenues = {
    sales[0][0]: sales[0][1] * sales[0][2],
    sales[1][0]: sales[1][1] * sales[1][2],
    sales[2][0]: sales[2][1] * sales[2][2]
}
print(sum(revenues.values()))
print(max(revenues, key=revenues.get))
print(revenues)
print({sales[0][1], sales[1][1], sales[2][1]})

print("Q44")
customers = {
    "C101": {"name": "Ali", "orders": [1200, 2500, 1800]},
    "C102": {"name": "Sara", "orders": [3000, 4500]},
    "C103": {"name": "Ahmed", "orders": [1500, 2000, 1000]}
}
totals = {
    "C101": sum(customers["C101"]["orders"]),
    "C102": sum(customers["C102"]["orders"]),
    "C103": sum(customers["C103"]["orders"])
}
top_id = max(totals, key=totals.get)
print(totals)
print(customers[top_id]["name"])
print((totals["C101"], totals["C102"], totals["C103"]))

print("Q45")
courses = {
    "Python": {"Ali", "Sara", "Ahmed"},
    "SQL": {"Sara", "Ahmed", "Zain"},
    "AWS": {"Ali", "Ahmed", "Zain"}
}
all_three = courses["Python"] & courses["SQL"] & courses["AWS"]
at_least_two = (courses["Python"] & courses["SQL"]) | (courses["Python"] & courses["AWS"]) | (courses["SQL"] & courses["AWS"])
all_students = courses["Python"] | courses["SQL"] | courses["AWS"]
print(at_least_two - all_three)
print(all_three)
print(all_students - at_least_two)
print(len(all_students))

print("Q46")
transactions = [
    {"id": 101, "customer": "Ali", "items": [("Laptop", 120000, 1), ("Mouse", 1500, 2)]},
    {"id": 102, "customer": "Sara", "items": [("Keyboard", 3500, 2), ("Mouse", 1500, 1)]},
    {"id": 103, "customer": "Ali", "items": [("Monitor", 45000, 1)]}
]
t1 = 120000 * 1 + 1500 * 2
t2 = 3500 * 2 + 1500 * 1
t3 = 45000 * 1
print(t1 + t2 + t3)
print(t1 + t3)
print(max(t1, t2, t3))
print({"Laptop", "Mouse", "Keyboard", "Monitor"})


print("Q47")
pipelines = {
    "pipeline_1": {"status": "success", "records": (1000, 1200, 1100)},
    "pipeline_2": {"status": "failed", "records": (800, 0, 0)},
    "pipeline_3": {"status": "success", "records": (1500, 1600, 1700)}
}
totals = {
    "pipeline_1": sum(pipelines["pipeline_1"]["records"]),
    "pipeline_2": sum(pipelines["pipeline_2"]["records"]),
    "pipeline_3": sum(pipelines["pipeline_3"]["records"])
}
averages = {
    "pipeline_1": totals["pipeline_1"] / len(pipelines["pipeline_1"]["records"]),
    "pipeline_2": totals["pipeline_2"] / len(pipelines["pipeline_2"]["records"]),
    "pipeline_3": totals["pipeline_3"] / len(pipelines["pipeline_3"]["records"])
}
print(sum(totals.values()))
print({"pipeline_2"} if pipelines["pipeline_2"]["status"] == "failed" else set())
print(max(totals, key=totals.get))
print(averages)

print("Q48")
accounts = {
    "A101": {"holder": "Ali", "transactions": [5000, -2000, 3000, -1000]},
    "A102": {"holder": "Sara", "transactions": [10000, -3000, -2000]},
    "A103": {"holder": "Ahmed", "transactions": [7000, -1500, 2500]}
}
balances = {
    "A101": sum(accounts["A101"]["transactions"]),
    "A102": sum(accounts["A102"]["transactions"]),
    "A103": sum(accounts["A103"]["transactions"])
}
print(balances)
highest_id = max(balances, key=balances.get)
print(accounts[highest_id]["holder"], balances[highest_id])
print(abs(-2000) + abs(-1000) + abs(-3000) + abs(-2000) + abs(-1500))
print(max(5000, 3000, 10000, 7000, 2500))

print("Q49")
users = {
    "Ali": {"purchased": {"Laptop", "Mouse"}, "wishlist": {"Keyboard", "Monitor", "Mouse"}},
    "Sara": {"purchased": {"Keyboard", "Monitor"}, "wishlist": {"Laptop", "Mouse"}},
    "Ahmed": {"purchased": {"Laptop", "Keyboard"}, "wishlist": {"Monitor", "Headphones"}}
}
bought_twice = (
    (users["Ali"]["purchased"] & users["Sara"]["purchased"])
    | (users["Ali"]["purchased"] & users["Ahmed"]["purchased"])
    | (users["Sara"]["purchased"] & users["Ahmed"]["purchased"])
)
print(bought_twice)
print(users["Ali"]["wishlist"] - users["Ali"]["purchased"])
print(users["Ali"]["wishlist"] & users["Sara"]["wishlist"] & users["Ahmed"]["wishlist"])
print(
    users["Ali"]["purchased"] | users["Ali"]["wishlist"]
    | users["Sara"]["purchased"] | users["Sara"]["wishlist"]
    | users["Ahmed"]["purchased"] | users["Ahmed"]["wishlist"]
)

print("Q50")
company = {
    "departments": {
        "Engineering": {
            "employees": [
                ("Ali", 120000, {"Python", "AWS", "SQL"}),
                ("Sara", 150000, {"Python", "Databricks", "SQL"})
            ],
            "budget": 500000
        },
        "Analytics": {
            "employees": [
                ("Ahmed", 100000, {"SQL", "Power BI"}),
                ("Zain", 130000, {"Python", "SQL", "Tableau"})
            ],
            "budget": 400000
        }
    }
}
eng = company["departments"]["Engineering"]
ana = company["departments"]["Analytics"]
eng_payroll = eng["employees"][0][1] + eng["employees"][1][1]
ana_payroll = ana["employees"][0][1] + ana["employees"][1][1]
print("Payroll:", eng_payroll, ana_payroll)
print("Company payroll:", eng_payroll + ana_payroll)

highest = eng["employees"][0]
highest = eng["employees"][1] if eng["employees"][1][1] > highest[1] else highest
highest = ana["employees"][0] if ana["employees"][0][1] > highest[1] else highest
highest = ana["employees"][1] if ana["employees"][1][1] > highest[1] else highest
print("Highest paid:", highest[0], highest[1])

shared = eng["employees"][0][2] & eng["employees"][1][2] & ana["employees"][0][2] & ana["employees"][1][2]
eng_only = (eng["employees"][0][2] | eng["employees"][1][2]) - (ana["employees"][0][2] | ana["employees"][1][2])
print("Shared skills:", shared)
print("Engineering only:", eng_only)
print("Remaining budgets:", eng["budget"] - eng_payroll, ana["budget"] - ana_payroll)

eng_avg = eng_payroll / len(eng["employees"])
ana_avg = ana_payroll / len(ana["employees"])
print("Higher average salary:", "Engineering" if eng_avg > ana_avg else "Analytics")

name_salary = {
    eng["employees"][0][0]: eng["employees"][0][1],
    eng["employees"][1][0]: eng["employees"][1][1],
    ana["employees"][0][0]: ana["employees"][0][1],
    ana["employees"][1][0]: ana["employees"][1][1]
}
all_skills = eng["employees"][0][2] | eng["employees"][1][2] | ana["employees"][0][2] | ana["employees"][1][2]
print("Name and salary:", name_salary)
print("All skills:", all_skills)
print("Combined budget enough:", eng["budget"] + ana["budget"] >= eng_payroll + ana_payroll)

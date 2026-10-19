# Sets practice (Q21-Q30)

print("Q21")
numbers = [10, 20, 10, 30, 40, 20, 50]
numbers_set = set(numbers)
print(numbers_set)
print(len(numbers_set))

print("Q22")
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

print("Q23")
skills = {"Python", "SQL", "AWS"}
skills.add("Snowflake")
skills.add("Databricks")
skills.discard("AWS")
print(skills)

print("Q24")
python_students = {"Ali", "Sara", "Ahmed", "Zain"}
sql_students = {"Sara", "Ahmed", "Hamza", "Usman"}
print(python_students & sql_students)
print(python_students ^ sql_students)

print("Q25")
required_skills = {"Python", "SQL"}
candidate_skills = {"Python", "SQL", "AWS", "Snowflake"}
print(required_skills.issubset(candidate_skills))
print(candidate_skills.issuperset(required_skills))

print("Q26")
numbers = {1, 2, 4, 6, 8, 10}
all_numbers = set(range(1, 11))
print(all_numbers - numbers)

print("Q27")
python = {"Ali", "Sara", "Ahmed", "Zain"}
sql = {"Sara", "Ahmed", "Hamza"}
aws = {"Ahmed", "Zain", "Hamza"}
print(python & sql & aws)
print((python & sql) - aws)
print((python & sql) | (python & aws) | (sql & aws))

print("Q28")
day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}
day3 = {104, 106, 107, 108}
print(day1 & day2 & day3)
print((day1 - day2 - day3) | (day2 - day1 - day3) | (day3 - day1 - day2))
print((day1 & day2) | (day1 & day3) | (day2 & day3))

print("Q29")
required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write", "delete"}
print(required_permissions - user_permissions)
print(user_permissions - required_permissions)
print(required_permissions.issubset(user_permissions))

print("Q30")
website = {"C1", "C2", "C3", "C4", "C5"}
mobile = {"C3", "C4", "C6", "C7"}
store = {"C2", "C4", "C7", "C8"}
all_three = website & mobile & store
at_least_two = (website & mobile) | (website & store) | (mobile & store)
exactly_two = at_least_two - all_three
exactly_one = (website | mobile | store) - at_least_two
print(exactly_one)
print(exactly_two)
print(all_three)

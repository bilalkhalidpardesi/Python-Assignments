# Tuples practice (Q11-Q20)

print("Q11")
colors = ("red", "green", "blue", "yellow", "purple")
print(colors[1])
print(colors[-1])
print(colors[1:4])

print("Q12")
employee = ("Ali", 28, "Data Engineer", 150000)
name, age, job, salary = employee
print(name, salary)

print("Q13")
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
combined = tuple1 + tuple2
print(combined)
print(combined[::-1])

print("Q14")
numbers = (10, 20, 30, 20, 40, 20, 50)
print(numbers.count(20))
print(numbers.index(20))

print("Q15")
data = (100, 200, 300, 400, 500, 600)
first, second, *middle, last = data
print(first, second, list(middle), last)

print("Q16")
numbers = (10, 20, 30, 40, 50)
new_numbers = numbers[:2] + (300,) + numbers[3:]
print(new_numbers)

print("Q17")
students = (
    ("Ali", (85, 90, 88)),
    ("Sara", (92, 87, 95)),
    ("Ahmed", (78, 84, 80))
)
print(students[1][1][1])
print(sum(students[0][1]) / len(students[0][1]))
print(max(students[2][1]))

print("Q18")
from operator import itemgetter
employees = (
    ("Ali", 80000),
    ("Sara", 120000),
    ("Ahmed", 95000)
)
print(tuple(sorted(employees, key=itemgetter(1), reverse=True)))

print("Q19")
matrix = ((2, 4, 6), (8, 10, 12), (14, 16, 18))
diagonal = (matrix[0][0], matrix[1][1], matrix[2][2])
product = diagonal[0] * diagonal[1] * diagonal[2]
row_sums = (sum(matrix[0]), sum(matrix[1]), sum(matrix[2]))
print(diagonal, product, row_sums)

print("Q20")
records = (
    ("Laptop", 120000, 5),
    ("Mouse", 1500, 20),
    ("Keyboard", 3500, 10)
)
total = records[0][1] * records[0][2] + records[1][1] * records[1][2] + records[2][1] * records[2][2]
expensive = max(records, key=itemgetter(1))
names = (records[-1][0], records[-2][0], records[-3][0])
print(total)
print(expensive)
print(names)

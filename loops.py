# 1. WHILE LOOP
counter = 0
while counter <= 15:
    print(counter)
    counter += 1

t = 90
while range(t, 80):
    print(t)
    t += 1

for xyz in range(90,80,-1):
    print(xyz)

# 1. Tuples
cars = ("mercedes", "R34", "Probox", "fielder", "crv")
print(cars)
print(cars[2])

# cars[0] = "mercedes" this is impossible

print(cars[1])
print(cars[1:4])
for gari in cars:
    print(gari)
# 2. Lists
colours = ["red", "green", "blue", "black", "indigo"]
print(colours)
print(colours[2])
colours[0] = "light red"
print(colours[0:4])
for rangi in colours:
    print(colours)
colours.reverse()
print(colours)
print(colours.pop(2))
print(colours)
# 3. Dictionaries
students = {"adm1": "tracy","adm2" : "becky", "adm3": "kisha"}
print(students["adm1"])
for funguo in students.keys():
    print(funguo)
for jina in students.values():
    print(jina)
# 4. Sets
ranks = {1, 5, 8, 4, 0, 9, 6, 2, 11, 12, 3, 10}
print(ranks)


names = ["kijana", "barobaro", "alienda", "akakula", "yule", "mnyama", "akatosheka"]
print(names)
print()





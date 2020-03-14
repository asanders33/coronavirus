import random as r

names = ["Alex", "Amanda", "Emma", "Penelope", "Josh", "Ben", "John", "Sofia", "Traci", "Jan"]
states = ["infected", "not infected"]
r.seed(1234)

people = []
for i in range(0, 100):
    name = names[int(r.random() * 10)]
    state = states[int(r.random() * 2)]
    age = int(r.random() * 100)
    people.append([name, state, age])

print(people)

for person in people:
    print(person)

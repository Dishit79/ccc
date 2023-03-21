n = int(input())
list1 = []
for i in range(n):
    list1.append(str(input()))

chilis = {"Poblano": 1500, "Mirasol": 6000, "Serrano": 15500, "Cayenne": 40000, "Thai": 75000, "Habanero":125000 }


final = 0
for spice in list1:
    final += chilis[spice]

print(final)
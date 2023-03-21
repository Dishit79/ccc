list1 = []
for i in range(2):
    list1.append(int(input()))


parcels = list1[0]
collisions = list1[1]


parcelsVal = parcels * 50
collisionsVal = collisions * 10


extra = 0

if parcels > collisions:
    extra = 500

final = parcelsVal - collisionsVal + extra
print(final)
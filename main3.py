n = int(input())
list1= []
for i in range(n):
    input3 = str(input())
    list1.append([*input3])
days = [0, 0, 0, 0, 0]

for i in (list1):
    for t, d in enumerate(i):
        if d == "Y":
            days[t] +=1
            


maxnum = max(days)
final = [i+1 for i, num in enumerate(days) if num == maxnum]

print(','.join(map(str, final)))
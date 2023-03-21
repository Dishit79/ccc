word = [*input().strip()]

rows = int(input().strip())
cols = int(input().strip())

grid = []
for i in range(rows):
    row = input().strip().split()
    grid.append(row)

count3 = 0 
count = 0
for t in grid:
    for u, i in enumerate(t):
        for y, l in enumerate(word):
            if t[u] == t[u]:
            
                count3 += 1
            else:
                pass
                

print(count3)
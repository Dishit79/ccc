n = int(input())
list1= []
for i in range(2):
    input3 = (input()).split(" ")
    t = [*input3]
    list1.append([int(x) for x in t])


sum1 = 0

for i, data in enumerate(list1[0]):

    if list1[0][i] == 1:
        if list1[0][i-1] == 1 and i-1 != -1:
            sum1 = sum1 + 2 - 1
            
        else:   
            sum1 += 3

y = sum1
# print(sum1)
for i, data in enumerate(list1[1]):

    if list1[1][i] == 1:
       
        # print(i)
       if (i +1) % 2 == 0:
            pass
       else:
        #    print (i +1 , "hit2")
           if list1[0][i] == 1:
               sum1 -= 2
       if list1[1][i-1] == 1 and i-1 != -1:
            # print("hit")
            sum1 = sum1 + 2 - 1

       else:   
            sum1 += 3
        



print(sum1)



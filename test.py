def calculate_tape_needed(cols, row1, row2):
    wet_areas = []
    # check the first tile of row1
    if row1[0] == 1:
        wet_areas.append([0, 0])
    # check the first tile of row2
    if row2[0] == 1:
        if wet_areas:
            # add the second tile of the first wet area
            wet_areas[-1][1] = 1
        else:
            # create a new wet area
            wet_areas.append([1, 1])
    # check the remaining tiles
    for i in range(1, cols):
        # check for a wet tile in row1
        if row1[i] == 1:
            if row1[i-1] == 1:
                # add the tile to the current wet area
                wet_areas[-1][1] = i
            elif row2[i] == 1:
                if wet_areas:
                    # add the tile to the current wet area
                    wet_areas[-1][1] = i
                else:
                    # create a new wet area
                    wet_areas.append([i, i])
        # check for a wet tile in row2
        elif row2[i] == 1:
            if row1[i] == 1:
                # add the tile to the current wet area
                wet_areas[-1][1] = i
            else:
                # create a new wet area
                wet_areas.append([i, i])
    # calculate the total length of tape needed
    total_tape = 0
    for area in wet_areas:
        # add the length of tape needed to surround the wet area
        total_tape += 2 + 2*(area[1] - area[0])
    return total_tape

# read the input values
n = int(input())
list1= []
for i in range(2):
    input3 = (input()).split(" ")
    t = [*input3]
    list1.append([int(x) for x in t])

# calculate the total length of tape needed
tape_needed = calculate_tape_needed(n, list1[0], list1[1])

# print the result
print(tape_needed)

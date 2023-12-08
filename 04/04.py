file = open("04/input.txt").readlines()


part_1 = 0

for lines in file:
    winning_numbers, my_numbers = [],[]
    points = 0
    
    lines = lines.rstrip().split("|")
    
    card_number = lines[0].split(":")[0].split(" ")[1] # not very neat
    winning = lines[0].split(":")[1].split(" ") 
    card = lines[1].split(" ")
    
    for element in winning:
        if element != "":
            winning_numbers.append(element)
            
    for element in card:
        if element != "":
            my_numbers.append(element)
    
    #part1
    temp = 0
    for number in my_numbers:
        if number in winning_numbers:
            temp += 1
    
    if temp != 0:
        part_1 += (2**(temp-1))
        
print(part_1)
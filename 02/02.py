file = open("02/input.txt").readlines()

MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14
part1 = 0
part2 = 0

for lines in file:
    temp, set_power = 0, 0
    
    local_max_blue, local_max_green, local_max_red = 0, 0, 0
    lines = lines.split(":")
    game_id = int(lines[0].split(" ")[1])
    games = lines[1].split(";")
    
    for game in games:
        hands = game.strip().split(", ")

        for hand in hands:
            number, color = int(hand.split(" ")[0]), hand.split(" ")[1]
            
            if color == "red" and number > MAX_RED or color == "green" and number > MAX_GREEN or color == "blue" and number > MAX_BLUE:
                temp = 1
    
            if color == "red" and number > local_max_red:
                local_max_red = number
            
            elif color == "green" and number > local_max_green:
                local_max_green = number
                
            if color == "blue" and number > local_max_blue:
                local_max_blue = number  
    
    if temp == 0:
        part1 += game_id          
        
    part2 += local_max_green*local_max_blue*local_max_red
    
print(part1)
print(part2)
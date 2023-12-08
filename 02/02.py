file = open("02/input.txt").readlines()

for lines in file:
    game_id = int((lines.split("Game")[1]).split(":")[0]) #questionable readability ¯\_(ツ)_/¯ 
    
file = open("06/input.txt").readlines()
#part 1 input
time = [int(item) for item in file[0].split(":")[1].split(" ") if item != '']
record = [int(item) for item in file[1].split(":")[1].split(" ") if item != '']

# part 2 input
real_time = int(''.join([item for item in file[0].split(":")[1].split(" ") if item != '']))
real_record = int(''.join([item for item in file[1].split(":")[1].split(" ") if item != '']))

part1 = 1
for i in range(len(time)):
    possible_wins = 0
    
    for ms in range(1, time[i]):
        distance = 1*ms*(time[i]-ms)
        if distance > record[i]:
            possible_wins += 1
    part1 *= possible_wins

part2 = 0 
for ms in range(1, real_time):
        distance = 1*ms*(real_time-ms)
        if distance > real_record:
            part2 += 1

print(f"Part 1: {part1}\nPart 2: {part2}")
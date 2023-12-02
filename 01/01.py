file = open("01/input.txt")
text = file.readlines()

#part 1
calibration_sum = 0
for lines in text:
    digits = []
    for char in lines:
        if char.isdigit():
            digits.append(int(char))
    calibration_sum += digits[0]*10 + digits[-1]
print(calibration_sum)        
    
        
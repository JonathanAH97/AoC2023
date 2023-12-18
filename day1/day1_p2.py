with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


# Find calibration value for a single line
# Search for the first number by going forwards in the string and stopping when a number is found
# Search for the second number by going backwards in the string and stopping when a number is found
def find_cal(line):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for s in line:
        if s.isdigit():
            first_num = s
            break

    for s in line[::-1]:
        if s.isdigit():
            second_num = s
            break

    return  int(first_num + second_num)

cal_list = [find_cal(line) for line in lines]
print(sum(cal_list))
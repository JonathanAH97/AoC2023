with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def find_number(s_5, reverse = False):
    numbers_dict_forward = {'one': '1', 'two': '2', 'three': '3',
                             'four': '4', 'five': '5', 'six': '6',
                               'seven': '7', 'eight': '8', 'nine': '9'}
    numbers_dict_reverse = {key[::-1]: value for key, value in numbers_dict_forward.items()}
    
    if reverse:
        numbers_dict = numbers_dict_reverse
    else:
        numbers_dict = numbers_dict_forward

    print(s_5)
    for number in numbers_dict:
        if number in s_5:
            index = s_5.find(number)
            if index == 0:
                print(number)
                print(numbers_dict[number])
                return numbers_dict[number]
    return None

def find_cal(line):

    for i,s in enumerate(line):

        find_num = find_number(line[i:i+5]) 

        if find_num is not None:
            first_num = find_num
            break
        if s.isdigit():
            first_num = s
            break

    for i,s in enumerate(line[::-1]):
        
        find_num = find_number(line[::-1][i:i+5], reverse = True)
        
        if find_num is not None:
            second_num = find_num
            break
        if s.isdigit():
            second_num = s
            break

    return  int(first_num + second_num)

cal_list = [find_cal(line) for line in lines]
print(sum(cal_list))
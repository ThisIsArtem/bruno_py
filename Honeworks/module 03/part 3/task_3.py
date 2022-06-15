def max_first_digit(lst_of_numbers):
    max_digit = 0
    max_digit_index = -1
    for i in range(len(lst_of_numbers)):
        if max_digit < int(str(lst_of_numbers[i])[0]):
            max_digit = int(str(lst_of_numbers[i])[0])
            max_digit_index = i
    return max_digit_index


def make_max_num(lst):
    max_number_str = ''
    for i in range(len(lst)):
        index = max_first_digit(lst)
        max_number_str += str(lst[index])
        lst.remove(lst[index])
    print(max_number_str)


make_max_num([56, 9, 11, 2])

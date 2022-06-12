string = 'My brother bought new car last yaer'
number_of_long_words = 0
current_len = 0
for i in range(len(string)):
    if 65 <= ord(string[i]) <= 122:
        current_len += 1
    else:
        if current_len > 4:
            number_of_long_words += 1
        current_len = 0
print(number_of_long_words)
number = input('Enter the number: ')
digit_sum = 0
for i in range(len(number)):
	digit_sum += int(number[i])
print(digit_sum)

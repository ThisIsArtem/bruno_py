number = int(input('Enter the number: '))
digit_sum = 0
while number > 0:
	digit_sum += number % 10
	number //= 10
print(digit_sum)

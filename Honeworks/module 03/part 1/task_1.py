deposit_amount = float(input('Enter the deposit amount: '))
deposit_interest = float(input('Enter the deposit interest: '))
target_amount = float(input('Enter the amount you want to receive: '))

deposit_validity_period = 0
while deposit_amount < target_amount:
	deposit_validity_period += 1
	deposit_amount += deposit_amount / 100 * deposit_interest
	deposit_amount = int(deposit_amount)
print('The amount you need will be accumulated in ' + str(deposit_validity_period) + ' years.')

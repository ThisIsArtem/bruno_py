def non_unique_items(lst):
	unique_items_lst = list(set(lst))
	new_dict = dict.fromkeys(unique_items_lst, 0)

	for i in range(len(lst)):
		new_dict[lst[i]] += 1

	non_unique_lst = []
	for i in range(len(new_dict)):
		if new_dict[unique_items_lst[i]] != 1:
			print(unique_items_lst[i], end = ' ')

non_unique_items([1, 12, 1, 23, 144, 12])

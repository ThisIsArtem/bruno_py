def max_in_lst(lst):
    max_num = lst[0][0]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if max_num < lst[i][j]:
                max_num = lst[i][j]
    print(max_num)


lst = [[1, 2, 4, 4], 
        [2, 7, 15, 9], 
        [9, 1, 16, 1]]
max_in_lst(lst)

def sum_three(my_list, n):
    found = False
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if (my_list[i] + my_list[j] + my_list[k] == 0):
                    print(my_list[i], my_list[j], my_list[k])
                    found = True

    if (found == False):
        print(" not exist ")


my_list = [-25, -18, -1, -5, 9, -4, 9, 10]
n = len(my_list)
sum_three(my_list, n)
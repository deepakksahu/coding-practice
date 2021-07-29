def intersection1(list_1, list_2):
    # your code goes here
    result = []
    for i in list_1:
        if i in list_2:
            result.append(i)
    print(list(set(result)))
    # return list(set(result)

intersection1([4, 9, 9, 11, 26, 28, 54, 69], [9, 9, 74, 21, 11, 63, 28, 26])
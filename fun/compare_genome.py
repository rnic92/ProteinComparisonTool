def comparisons(str1, str2):
    size = min([len(str1), len(str2)])
    dif = []
    change = "Mutation"
    print(len(str1), len(str2))
    for i in range(size):
        if str1[i] != str2[i]:
            dif.append((i+1, str1[i], str2[i]))
    if len(str1) > len(str2):
        change = "Possible deletion"
        for i in range(len(str2), len(str1)):
            dif.append((i+1, str1[i], " "))
    elif len(str1) < len(str2):
        change = "Possible insertion"
        for i in range(len(str1),len(str2)): # 1 value
            dif.append((i+1, " ", str2[i]))
    return change, dif

from compare_genome import comparisons

# print(comparisons("qbbd", "ab"))

x = [('a',1), ('b',2), ('c',3), ('d',4)]

with open('results.txt', 'w') as f:
    for i in x:
        for item in i:
            f.write(str(item))
            f.write(' ')
        f.write(', ')

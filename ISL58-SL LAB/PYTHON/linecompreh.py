S = [x**2 for x in range(10)]# read elements to list
M = [x for x in S if x % 2 == 0 ]
M.reverse()
print(M)

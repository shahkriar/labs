# EX1
i = 1
while i < 6:
    print(i)
    i += 1
    
# EX2
i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1
    
# EX3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    
# EX4
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
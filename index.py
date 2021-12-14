# name = 'Otabek'
# name = name.upper()
# print(name)

# print(name.index('e', 1, 2))
# name = name[3].isalpha()
# print(name)
# name = name.rstrip()


# Task 1 ----------------------------------------
# str = ''
# i = 0
# for ltr in 'Elbek':
#     if i % 2 == 0: str += ltr.upper()
#     else: str += ltr
#     i += 1
# print(str)

# str = ''
# for i, ltr in enumerate('Elbek', 1):  # inversiya 
                                # i, letter = (0, 'E')
                                # i, latter = (1, 'l') -> (index, 'element')
    # if i % 2 == 0: str += ltr.upper()
    # else: str += ltr.lower()
# print(str)




# Task 2 -------------------------------------------------
# str = ''
# for i, ltr in enumerate('Elbek'):
    # str = ltr + str
# print(str[::-1])
# print(str)

# str = 'Hello'
# str2 = ''
# for ltr in str:
#     str2 = ltr + str2
# print(str2)

# str = 'Hello'
# str2 = ''
# for i in range(len(str) - 1, -1, -1):
#     str2 += str[i]
# print(str2)

# nameList = list('Elbek')
# nameList.reverse()
# str = ''.join(nameList)
# print(str)



# Task 3 ----------------------------------
# nums = [1, 2, 3]
# t = tuple(nums)
# print(t)



# Task 4 -------------------------------------
# print([elem for elem in range(10)])
# print([elem for elem in range(10) if elem % 2 == 0])



# Task 5 --------------------------------------
# import random
# print(random.random())

from random import random
from random import randint
# from datetime import datetime as d

from datetime import datetime, date
from datetime import datetime as d, date as dt

# print(random() * 255)
# print(int(random() * 255)) # 4 steps
# print(randint(0, 255)) # 2 steps

# print(round(100 + random() * (200 - 100)))

print(d.now())
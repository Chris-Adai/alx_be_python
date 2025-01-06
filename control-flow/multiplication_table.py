# print (range(10))

# # for i in range(10):
# #     print (i)

# for i in range (11):
#     print (i)

# print (range(11))

# print (range (1,11))

# this priogram block produces the output, 5 x 1 = 5  :  
# 5 x 2 = 55   
# 5 x 3 = 555  
# 5 x 4 = 5555 
# 5 x 5 = 55555
# 5 x 6 = 555555
# 5 x 7 = 5555555
# 5 x 8 = 55555555
# 5 x 9 = 555555555
# 5 x 10 = 5555555555
# which can be used for the right angle triangle problem

# number = input ('Enter a number to see its multiplication table: ' )   # could not using int(input())

# for i in range (1,11):
#     mult_num = number * i
#     print (f'{number} x {i} = {mult_num}')

number = int(input('Enter a number to see its multiplication table: ' )) # try doing this with different datatypes especially float

for i in range(1,11):
   # multi_num = number * i
    # print(f"{number} x {i} = {multi_num}")
    print(f"{number} x {i} = {number * i}")





# note: the reason why this didnt work is because i diddnt use the IN function or for ... in ...
# this didnt produce the desired result 
# symbol_number = int(input('Enter the size of the pattern: ' ))

# # i=1

# sym = "*"

# while i <= symbol_number:
#     # try first initialization here
#     i=0
#     print (sym * symbol_number)
#     # i +=1
#     # break

#     # try if if i

# ------------------------------------------------------------------------

# try this using for loops alone ; try using for loops nested with if statement
# solution: try using for loops nested with while loops

#-------------------------------------------------------------------------


symbol_number =int(input('Enter the size of the pattern: ' ))

# loop_sym_num = range (symbol_number + 1)  # this is producing +1 higher than the normal . why?

loop_sym_num = range (symbol_number)  

sym = "*"

for i in loop_sym_num:
    # j=0
    # while j <= symbol_number:
    while i <= symbol_number:
        print (sym * symbol_number )
            # print ()
        break
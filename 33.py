# hairs = ['brown', 'blond', 'red']
# eyes = ['brown', 'blue', 'green']
# weights = [1, 2, 3, 4]

# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for number in the_count:
#     print(f"This is count {number}")

# for fruit in fruits:
#     print(f"A fruit of type: {fruit}")

# for i in change:
#     print(f"I got {i}")

# elements = []

# for i in range(0, 6):
#     print(f"Adding {i} to the list")
#     elements.append(i)

# for i in elements:
#     print(f"Element was: {i}")

# from dis import dis

# dis('''
# for number in the_count:
#         print(number)
# ''')

##### RESULT
#   0           0 RESUME                   0                

#   2           2 LOAD_NAME                0 (the_count)    # get the_count list
#               4 GET_ITER                                  # start iteration
#         >>    6 FOR_ITER                10 (to 30)        # for-loop jump to 18
#              10 STORE_NAME               1 (number)       # create number variable

#   3          12 PUSH_NULL
#              14 LOAD_NAME                2 (print)        # load print()
#              16 LOAD_NAME                1 (number)       # load number
#              18 CALL                     1                # call print()
#              26 POP_TOP                                   # clean stack
#              28 JUMP_BACKWARD           12 (to 6)         # jump back to FOR_ITER at 6

#   2     >>   30 END_FOR                                   # end the for loop when it is done
#              32 RETURN_CONST             0 (None)         

# _count.__next__()
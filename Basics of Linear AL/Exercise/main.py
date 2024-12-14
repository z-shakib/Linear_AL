#! Scalers and vectors:
v = [5,10,15,20]
#! Multiply each element by 2
v_multiply = [x*2 for x in v]
print(f'Multiply each element by 2 is:\n {v_multiply}')

#! add 5 to each element:
v_adding = [x+5 for x in v]
print(f'add 5 to each element is: \n {v_adding}')

#! Find the sum of all numbers :
v_sum = sum(v)
print(f'the sum of all number is: \n {v_sum}')

# Numbers
print('\n-----------------Numbers----------------')
## type - int
print('5 ->', type(5))
## type - float
print('3.6 ->', type(3.6))
## type - complex
print('2j -> ', type(2j))



# Memory Locations - Pass by value example
print('\n-----------------Memory Locations----------------')
a = 4
print('a=',a,', location id =', id(a))
b = a
print('b=',b, ', location id =', id(b))
a = 10
print('a=',a ,', location id =', id(a), '|  b=',b, ', location id =', id(b))

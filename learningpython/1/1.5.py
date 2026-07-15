#CONDITIONAL OPERATORS
x = 7
y = 8
z = 0

result1 = x == y #checks if x and y are equal
result2 = y > x
result3 = z < x + 2

result4= result1 or result2 #checks if either result1 or result2 is true
print(result4) #True because result2 is true
print(not False) #True
print(not True) #False
print(not (False and True)) #True because not reverses the result of the statement
#order of operations: not, and, or


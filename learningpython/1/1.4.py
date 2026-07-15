#CONDITIONS
# == #checks if two values are equal
# != #checks if two values are not equal
# <= #checks if left value is less than or equal to right value
# >= #checks if left value is greater than or equal to right value
# < #checks if left value is less than right value
#> #checks if left value is greater than right value

x = 'hello'
y = 'hello'
print(x==y) #True
print (x != y) #False

print('a' < 'Z')#True because every letter has a value in the ASCII table, and a is greater than Z
print(ord('a'))#returns 97
print(ord('Z'))#returns 90

print(7.5 <= 7.5)#True
print(7.5 >= 7.5)#True
print(7.5 < 7.5)#False
print(7.5 > 7.5)#False 

result = 6 == 6
print(result) #True
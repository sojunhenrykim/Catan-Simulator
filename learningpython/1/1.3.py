#STRING METHODS
hello = 'hello'
print(type(hello)) #returns class
#method: operator with a dot
hello= 'hello' .upper() #returns HELLO
hello= 'hello' .lower() #returns hello

hello = 'hellO woRld'
print(hello.capitalize())# capitalizes like english
print(hello.count('l'))#counts how many l's are in the string

#String Multiplication
x= 'hello '
print(x*3) #prints hello 3 times
y= 'yes'
print(x+y*3) #prints hello yesyesyes

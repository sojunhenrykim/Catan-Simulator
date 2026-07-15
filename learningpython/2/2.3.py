#SCOPE AND GLOBAL
x = 'tim' 
def func(name):
    x = name#this is in the scope of the function, so 
print(x)#this will not call name
func('changed')
print(x)

def func(name):
    global x#not good to use
    x = name#this is now global
print(x)#this will call name
func('changed')
print(x)

#Rasing an exception
raise Exception('Bad')
raise FileExistsError('')

#HANDLING EXCEPTIONS
try:
    x = 7/0
except Exception as e:
    print(e)
finally:
    print('finally')

#Lambdas
x = lambda x: x+5
print(x(2))

#Map and filter
x = [1,2,3,4,12,3,213,1,]
mp = map(lambda i: i+2, x)#adds 2 to everything
print(list(mp))#prints mp as a list

mp = filter(lambda i: i%2==0, x)#filters even numbers
print(list(mp)) 

#F STRINGS
tim =89 #THIS IS SUPER COOL
x = f'hello {6 + 8} {tim}'




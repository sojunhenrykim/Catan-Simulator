#UNPACK OPERATOR
def func(x):
    def func2():
        print(x)

    return func2
func(3)() #prints 3 second braket calls it

#ARGS AND KWARGS *Args *Kwargs
x = [1, 23, 236363, 2727]
print (*x) #prints 1 23 236363 2727, unpacks the list and prints each element

def func3(x, y):
    print(x,y)
pairs = [(1,2), (3,4), (5,6)]
for pair in pairs:
    func3(*pair) #unpacks the pair and passes it to the function, prints 1 2, 3 4, 5 6
    func3(**{'x': 1, 'y': 2}) #unpacks the dictionary and passes it to the function, prints 1 2
#Args are used to get a tuple
#Kwargs are used to get a dictionary

def func4(*args, **kwargs):
    print(args, kwargs)
func4(1,2,3,4,5,one=0,two=1)#collects arguements and makes tuple and dictionary





#FUNCTIONS IN PYTHON
def func():#defines a function with name func
    print('Run')

func()#calls the function

def func1(x, y):
    print(x + y)
    return x + y, x-y #returns a tuple

func1(5, 6)#calls the function with x=5 and y=6, will print 11
r1, r2 = func(5, 6)#calls the function with x=5 and y=6, will print 11, r1 will be 11 and r2 will be -1
print(r1, r2)




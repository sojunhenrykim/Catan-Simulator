#COLLECTIONS
#collection is a both ordered and unordered set
x = [4, True, 'hi'] #list-ordered, mutable
print(len(x)) #returns 3- how many items are in the list
x.append('hello') #adds hello to the end of the list
x.extend([4,5,5,5])# adds 4,5,5,5 to the end of the list
x.pop() #removes the last item in the list
x.pop(0) #removes the first item in the list
#indexes are counted from 0
#last index: len(x)-1
print(x[1]) #returns the first item in the list
x[0] = 'hi' #changes the first item in the list to hi
y = x#x and y share a reference, not a copy
#if a change is made to x, so will y, and vice versa

x = (4, True, 'hi') #tuple-ordered, immutable
print(x[0]) #returns the first item in the tuple

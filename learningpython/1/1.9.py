#SLICE OPERATOR
x = [1,2,3,4,5]
y = ['hi', 'hello', 'bye', 'goodbye']
s = 'hello world'
sliced = x[start:stop:step] #slices the list from start to stop with step
#start is included, stop is not
sliced = x[::-1]#easy way to reverse a list

#SETS
s = {1, 2, 3, 4, 5} #creates a set
#for empty set, use s = set()
#duplicates are automatically removed from a set
s.add(6) #adds 6 to the set
s.remove(6) #removes 6 from the set
s2 = {4, 5, 6, 7, 8}
print(4 in s) #True

print(s.union(s2)) #returns a set with all elements from both sets
print(s.intersection(s2)) #returns a set with elements that are in both sets
print(s.difference(s2)) #returns a set with elements that are in s but not in s2

#Dictionaries
x = {'key' : 4} #creates a dictionary with key 'key' and value 4
x['key2'] = 5 #adds key2 to the dictionary with value 5
x[2] = {2,2,1}#any value works

print('key' in x) #True
print(x.values()) #returns a view of all values in the dictionary   
print(x.keys()) #returns a view of all keys in the dictionary
print(list(x.values()))
del x['key'] #removes key from the dictionary' \

for key, value in x.items():
    print(key, value)

for key in x:
    print(key, x[key])



      

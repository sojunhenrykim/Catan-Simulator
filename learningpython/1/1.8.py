#LOOPS
for i in range(10):#repeat a set time
    print(i) #prints 0-9
# 1 arguement; stop(starts at 0
# 2 arguements; start, stop
# 3 arguements; start, stop, step

for k in range(1, 11, 2):
    print(k) #prints 1,3,5,7,9

for j in [1,2,3,5]:
    print(j) #prints 1,2,3,5

x = [3,4,5,4,3]
for n in range(len(x)):
    print(x[n])
for n, element in enumerate(x):
    print(n, element) #prints index and value of each element in x

m = 0
while True:#repeat indefinitely
    print('run')
    m+=1
    if m == 10:
        break

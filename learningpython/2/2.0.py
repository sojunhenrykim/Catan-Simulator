#COMPREHENSIONS
x = [x +5 for x in range(5)]
print(x) #prints [5,6,7,8,9]

y = [i for i in range(100) if i % 5 ==0]
print(y) #prints all numbers from 0-100 that are divisible by 5


n = int(input("Number: "))
a = 1
b = 1
i = 1

print(a,", ", b, ", ", end = "")
while i<=n:
    b = a + b
    a = b - a
    i+=1
    print(b, ", ", end="")



    


x = [[1,2],[3,4]]
y = list(input())
n = len(y)
for i in range (n):
    if y[i]=='H':
        x = [x[1], x[0]]
    elif y[i]=='V':
        x[0] = [x[0][1],x[0][0]]
        x[1] = [x[1][1],x[1][0]]
    else:
        print("Invalid input")
        break




print(f'{x[0][0]} {x[0][1]}\n{x[1][0]} {x[1][1]}')
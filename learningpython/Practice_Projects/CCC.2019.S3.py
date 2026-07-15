import random
x = []
for i in range (3):
    z = input().split()
    for k in range (3):
        if z[k] != 'x':
            z[k] = int(z[k])
    x.append(z)



def horizantal(row):
    if (x[row].count('x')) == 1:
        for m in range (3):
            if x[row][m] == 'x':
                if m == 0:
                    x[row][m] = 2*(x[row][1])-x[row][2]
                if m == 1:
                    if (x[row][0]+x[row][2])%2 == 0:
                        x[row][m] = int(((x[row][0])+x[row][2])/2)
                    else:
                        return ("horizantal not done")
                if m== 2:
                    x[row][m] = 2*(x[row][1])-x[row][0]
                return ("horizantal done")
            else:
                continue
    elif (x[row].count('x')) == 2: 
        return ("horizantal not done")
    elif (x[row].count('x')) == 3:
        return ("horizantal not done")
    else:
        if (x[row][0]+x[row][2])%2 == 0:
            if x[row][1] == int((x[row][0]+x[row][2])/2):
                return ('horizantal done')
            else:
                return ("horizantal not done")
        else:
            return ("horizantal not done")

    

def vertical(column):
    y = [x[0][column], x[1][column], x[2][column]]
    if (y.count('x')) == 1:
        for m in range (3):
            if y[m] == 'x':
                if m == 0:
                    y[m] = 2*(y[1])-y[2]
                if m == 1:
                    if (y[0]+y[2])%2 == 0:
                        y[m] = int(((y[0])+y[2])/2)
                    else:
                        return ("vertical not done")
                if m== 2:
                    y[m] = 2*(y[1])-y[0]
                for k in range (3):
                    x[k][column] = y[k]
                return ("vertical done")
            else:
                continue
    elif (y.count('x')) == 2: 
            return ("vertical not done")
    elif (y.count('x')) == 3:
        return ("vertical not done")
    else:
        if (y[0]+y[2])%2 == 0:
            if y[1] == int((y[0]+y[2])/2):
                return ('vertical done')
            else:
                return ('vertical not done')
        else: 
            return ("vertical not done")

def horizantalcheck(m):
    if all(type(x[m][i]) == int for i in range (3)):
        if 2*x[m][1] == x[m][0]+x[m][2]:
            return('horizantal done')
        else:
            return('horizantal not done')
    else:
        return('horizantal not done')

def verticalcheck(n):
    if all(type(x[i][n]) == int for i in range (3)):
        if 2*x[1][n] == x[0][n]+x[2][n]:
            return('vertical done')
        else:
            return('vertical not done')
    else:
        return('vertical not done')


def fuckingannoyingcase(m):
    for k in range (3):
        if all(type(x[i][k]) == int for i in range (3)):
            for i in range (3):
                x[i] = [x[i][k], x[i][k], x[i][k]]
        elif all(type(x[k][i]) == int for i in range (3)):
            for i in range(3):
                x[k+1][i] = x[k][i]
                x[k+2][i] = x[k][i]


     


fullydone = 0
while fullydone == 0:
    q = []
    r = []
    if all((x[i].count('x')) == 3 for i in range (3) ):
        for i in range (3):
            for j in range (3):
                x[i][j] = 1
    elif all([type(x[i][0]),type(x[i][1]),type(x[i][2])]==[int, str, str] for i in range (3)):
        for k in range (3):
            x[k] = [x[k][0], x[k][0], x[k][0]]
    elif all([type(x[i][0]),type(x[i][1]),type(x[i][2])]==[str, int, str] for i in range (3)):
        for k in range (3):
            x[k] = [x[k][1], x[k][1], x[k][1]]
    elif all([type(x[i][0]),type(x[i][1]),type(x[i][2])]==[str, str, int] for i in range (3)):
        for k in range (3):
         x[k] = [x[k][2], x[k][2], x[k][2]]
    elif all([type(x[i][k]) for k in range (3)] == [int,int,int] and [type(x[i-1][k]) for j in range (3)] == [str, str, str] and [type(x[i-2][k]) for k in range (3)] == [str, str, str] for i in range (3)):
        for k in range (3):
            x[i-1][k] = x[i][k]
            x[i-2][k] = x[i][k]
    elif all([type(x[0][k]) for k in range (3)] == [int, str, str] and [type(x[1][k]) for k in range (3)] == [str, int, str] and [type(x[2][k]) for k in range (3)] == [str, str, int]):
        a = x[0][0]
        b = x[1][1]
        c = x[2][2]
        if 2*b == a+c:
            x[0]=[a,a,a]
            x[1]=[b,b,b]
            x[2]=[c,c,c]
        elif (a+c)%2 == 0:
            x[0]=[a, 2*b-c, -a+4*b-2*c]
            x[1]=[(a+c)/2,b,2*b-(a+c)/2]
            x[2]=[c,c,c]
        else: pass
    elif all([type(x[2][k]) for k in range (3)] == [int, str, str] and [type(x[1][k]) for k in range (3)] == [str, int, str] and [type(x[0][k]) for k in range (3)] == [str, str, int]):
        a = x[0][2]
        b = x[1][1]
        c = x[2][0]
        if 2*b == a+c:
            x[0]=[a,a,a]
            x[1]=[b,b,b]
            x[2]=[c,c,c]
        elif (a+c)%2 == 0:
            x[0]=[a, a, a]
            x[1]=[(a+c)/2,b,2*b-(a+c)/2]
            x[2]=[c,2*b-a,-c+4*b-2*a]
        else: pass
    elif all([type(x[0][k]) for k in range (3)] == [int, str, str] and [type(x[1][k]) for k in range (3)] == [str, str, int] and [type(x[2][k]) for k in range (3)] == [str, int, str]):
        a = x[0][0]
        b = x[1][2]
        c = x[2][1]
        if 2*c == b+a:
            x[0]=[a,c,b]
            x[1]=[a,c,b]
            x[2]=[a,c,b]
        elif 2*b == a+ c:
            x[0]=[a,a,a]
            x[1]=[b,b,b]
            x[2]=[c,c,c]
        else:
            x[0]=[a,2*b-c,4*b-2*c-a]
            x[1]=[5*b-2*a-2*c,3*b-a-c,b]
            x[2]=[c,c,c]
    elif all([type(x[0][k]) for k in range (3)] == [str, str, int] and [type(x[1][k]) for k in range (3)] == [int, str, str] and [type(x[2][k]) for k in range (3)] == [str, int, str]):
        a = x[0][2]
        b = x[1][0]
        c = x[2][1]
        if 2*c == b+a:
            x[0]=[b,c,a]
            x[1]=[b,c,a]
            x[2]=[b,c,a]
        elif 2*b == a+ c:
            x[0]=[a,a,a]
            x[1]=[b,b,b]
            x[2]=[c,c,c]
        else:
            x[0]=[4*b-2*c-a,2*b-c,a]
            x[1]=[b,3*b-a-c,5*b-2*a-2*c]
            x[2]=[c,c,c]
    elif all([type(x[0][k]) for k in range (3)] == [str, int, str] and [type(x[1][k]) for k in range (3)] == [str, str, int] and [type(x[2][k]) for k in range (3)] == [int, str, str]):
        a = x[0][1]
        b = x[1][2]
        c = x[2][0]
        if 2*b == a+ c:
            x[0]=[a,a,a]
            x[1]=[b,b,b]
            x[2]=[c,c,c]
        elif 2*a==b+c:
            x[0]=[c,a,b]
            x[1]=[c,a,b]
            x[2]=[c,a,b]
        else:    
            x[0]=[2*b-c,a,2*a-2*b+c]
            x[1]=[b,b,b]
            x[2]=[c,2*b-a,4*b-2*a-c]
    elif all([type(x[0][k]) for k in range (3)] == [str, int, str] and [type(x[1][k]) for k in range (3)] == [int, str, str] and [type(x[2][k]) for k in range (3)] == [str, str, int]):
        a = x[0][1]
        b = x[1][0]
        c = x[2][2]
        if 2*b == a+ c:
            x[0]=[a,a,a]
            x[1]=[b,b,b]
            x[2]=[c,c,c]
        elif 2*a==b+c:
            x[0]=[b,a,c]
            x[1]=[b,a,c]
            x[2]=[b,a,c]
        else:    
            x[0]=[2*a-2*b+c,a,2*b-c]
            x[1]=[b,b,b]
            x[2]=[4*b-2*a-c,c]
    else:
        continue
          
    for k in range (3):
        horizantal(k)
    for k in range (3):
        vertical(k)
    for k in range (3):
        q.append(horizantalcheck(k))
        r.append(verticalcheck(k))
    if all(q[k] == "horizantal done" for k in range (3)) and all(r[k] == 'vertical done' for k in range (3)):
        fullydone = 1
    else: continue





            
print(f'\n{x[0][0]} {x[0][1]} {x[0][2]}\n{x[1][0]} {x[1][1]} {x[1][2]}\n{x[2][0]} {x[2][1]} {x[2][2]}')






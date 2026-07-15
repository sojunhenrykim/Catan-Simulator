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
                    x[row][m] = int(((x[row][0])+x[row][2])/2)
                if m== 2:
                    x[row][m] = 2*(x[row][1])-x[row][0]
                return ("horizantal not done")
            else:
                continue
    elif (x[row].count('x')) == 2: 
        for m in range (3):
            if type(x[row][m]) == int:
                if m == 0:
                    x[row][1] = x[row][m]
                    x[row][2] = x[row][m]
                if m == 1:
                    x[row][0] = x[row][m]
                    x[row][2] = x[row][m]
                if m == 2:
                    x[row][0] = x[row][m]
                    x[row][1] = x[row][m]
                return ("horizantal not done")
            else:
                continue
    elif (x[row].count('x')) == 3:
        return ("horizantal not done")
    else:
        return ('horizantal done')
    

def vertical(column):
    y = []
    for k in range (3):
        y.append([x[0][k], x[1][k], x[2][k]])

    if (y[column].count('x')) == 1:
        for m in range (3):
            if y[column][m] == 'x':
                if m == 0:
                    y[column][m] = 2*(y[column][1])-y[column][2]
                if m == 1:
                    y[column][m] = int(((y[column][0])+y[column][2])/2)
                if m== 2:
                    y[column][m] = 2*(y[column][1])-y[column][0]
                for k in range (3):
                    for l in range (3):
                        x[k][l] = y[l][k]
                return ("vertical not done")
            else:
                continue
    elif (y[column].count('x')) == 2: 
        for m in range (3):
            if type(y[column][m]) == int:
                if m == 0:
                    y[column][1] = y[column][m]
                    y[column][2] = y[column][m]
                if m == 1:
                    y[column][0] = y[column][m]
                    y[column][2] = y[column][m]
                if m == 2:
                    y[column][0] = y[column][m]
                    y[column][1] = y[column][m]
                for k in range (3):
                    for l in range (3):
                        x[k][l] = y[l][k]
                return ("vertical not done")
            else:
                continue
    elif (y[column].count('x')) == 3:
        for k in range (3):
                    for l in range (3):
                        x[k][l] = y[l][k]
        return ("vertical not done")
    else:
        for k in range (3):
                    for l in range (3):
                        x[k][l] = y[l][k]
        return ('vertical done')


fullydone = 0
while fullydone == 0:
    a = []
    b = []
    for k in range (3):
        a.append(horizantal(k))
    for m in range (3):
        b.append(vertical(m))
    if all(a[k] == "horizantal done" for k in range (3)) and all(b[k] == 'vertical done' for k in range (3)):
        fullydone = 1
    else: continue





            
print(f'\n{x[0][0]} {x[0][1]} {x[0][2]}\n{x[1][0]} {x[1][1]} {x[1][2]}\n{x[2][0]} {x[2][1]} {x[2][2]}')






def matrixmul(a:list[list[int|float]],b:list[list[int|float]])-> list[list[int|float]]:
    if (len(a[0]) == len(b)):
        c = []
        for k in range(len(b)):
            x =[]
            for i in range(len(a)):
                sum = 0 
                for j in range(len(b)):
                        sum += a[i][j] * b[j][k]
                x.append(sum)
            c.append(x)
        c = [list(i) for i in zip(*c)]

        return c
    else:
        return -1
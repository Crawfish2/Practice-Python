zahyo = int(input())
sirusi = [input().split() for i in range(zahyo)]
for i in range(zahyo):
    for j in range(zahyo):
        flag = True
        for k in range(zahyo):
            if sirusi[i][k] != sirusi[k][j]:
                flag = False
                break
        if flag:
            print(i+1,j+1)

    

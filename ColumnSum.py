def columnsum(mat,row,col):

    result=[]
    for i in range(col):
        sum=0
        for j in range(row):
            sum+=mat[j][i]
        result.append(sum)
    return result

mat=[]
row=int(input("No of rows : "))
col=int(input("No of columns : "))
for i in range(row):
    mat.append(list(map(int,input().split())))

print(columnsum(mat,row,col))
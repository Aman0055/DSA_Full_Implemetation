def transpose():
    matrix =[
        [1,2,3,10],[4,5,6,11],[7,8,9,12],[13,14,15,16]
    ]
    print(len(matrix))
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            if i==j:continue
            else:
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        
    print(matrix)
transpose()
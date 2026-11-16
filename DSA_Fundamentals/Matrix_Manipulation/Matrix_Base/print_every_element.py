def print_every_element():
    matrix = [
        [1,2,3], [4,5,6]
    ]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()
print_every_element()
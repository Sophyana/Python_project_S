def multiply_matrices(mat1, mat2, size):
    result = [[0] * size for t in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


def print_matrix(matrix):
    for row in matrix:
        print(','.join(map(str, row)))


matrix = []
while line := input():
    matrix.append( [int(x) for x in eval(line)])
    check_len = [int(x) for x in eval(line)]
    if len(check_len) > 100:
        print("dimension more than possible")
        exit()


n = len(matrix) // 2
if n > 100:
    print("dimension more than possible")
    exit()
a = []
b = []
for i in range(n):
    a.append(matrix[i])
    b.append(matrix[n + i])

product = multiply_matrices(a, b, n)
print_matrix(product)


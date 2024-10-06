def get_matrix(n, m, value):
    matrix = []
    if n <= 0 or m <= 0 or value <= 0: # Если одно из значений будет равно или меньше 0,
        return matrix                  # будет возвращаться пустой список
    else:
        for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[len(matrix) - 1].append(value)
        return matrix

n_ = int(input('n >> '))
m_ = int(input('m >> '))
value_ = int(input('value >> '))
result_input = get_matrix(n_, m_, value_)
print(result_input)
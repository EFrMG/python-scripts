def adjacency_list_to_matrix(dict_in):
    n = len(dict_in)
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for node, neighbors in dict_in.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    for row in matrix:
        print(row)

    return matrix


def adjacency_matrix_to_list(matrix):
    adj_list = {}
    for i, row in enumerate(matrix):
        neighbors = []
        for j, val in enumerate(row):
            if val == 1:
                neighbors.append(j)
        adj_list[i] = neighbors
    return adj_list

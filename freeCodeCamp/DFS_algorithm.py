def dfs(adj_matrix, node_label):
    stack = [node_label]
    visited = []

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.append(current_node)

            for neighbor, is_connected in enumerate(adj_matrix[current_node]):
                if is_connected and neighbor not in visited:
                    stack.append(neighbor)

    return visited

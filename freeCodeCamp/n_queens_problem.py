def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []

    def solve(row, current_solution, cols, pos_diag, neg_diag):
        if row == n:
            solutions.append(list(current_solution))
            return

        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            current_solution.append(col)

            solve(row + 1, current_solution, cols, pos_diag, neg_diag)

            # Backtrack!
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)
            current_solution.pop()

    solve(0, [], set(), set(), set())
    return solutions

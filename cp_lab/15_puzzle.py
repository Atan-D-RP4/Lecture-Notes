def is_solvable(puzzle: list[list[int]]) -> bool:
    flat = [num for row in puzzle for num in row if num != 0]

    inv_count = 0
    for i in range(len(flat)):
        for j in range(i+1, len(flat)):
            if flat[i] > flat[j]:
                inv_count += 1

        zero_row = 4 - [row.count(0) for row in puzzle[::-1]].index(1) - 1

    if len(puzzle) % 2 == 1:
        return inv_count % 2 == 0
    else:
        if zero_row % 2 == 0:
            return inv_count % 2 == 1
        else:
            return inv_count % 2 == 0

def fifteen_puzzle(board: list[list[int]]):
    def get_empty_cell(board: list[list[int]]) -> tuple[int, int]:
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    return i, j
        raise ValueError("No empty cell found in the board")

    def is_valid_move(x: int, y: int) -> bool:
        return 0 <= x < 4 and 0 <= y < 4

    def get_moves(board: list[list[int]], x: int, y: int):
        moves = []
        directions = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
        for dx, dy, move_char in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y):
                new_board = [row[:] for row in board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                moves.append((new_board, move_char))
        return moves

    def solve(board: list[list[int]], max_depth=10):
        goal = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        queue = [(board, '', 0)]
        visited = set()

        while queue:
            board, path, depth = queue.pop(0)

            if board == goal:
                return list(path)

            if depth >= max_depth:
                return None

            x, y = get_empty_cell(board)
            for new_board, move in get_moves(board, x, y):
                board_str = str(new_board)
                if board_str not in visited:
                    visited.add(board_str)
                    queue.append((new_board, path + move, depth + 1))

        return None  # No solution found

    return solve(board)

def main() -> None:
    # Read number of test cases
    n = int(input())

    # Process each puzzle
    for _ in range(n):
        # Read puzzle
        puzzle = []
        for __ in range(4):
            puzzle.append(list(map(int, input().split())))

        if is_solvable(puzzle) is False:
            print("This puzzle is not Solvable.")
            return

        # Solve puzzle
        solution = fifteen_puzzle(puzzle)

        # Output
        if solution is None:
            print("This puzzle is not solvable.")
        else:
            print(len(solution))
            print(''.join(solution))

# Run the main function
if __name__ == "__main__":
    main()

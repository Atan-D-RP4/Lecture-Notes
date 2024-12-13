# Traversing a matrix in a spiral order
def spiral_matrix_traversal(mat: list[list[int]]) -> None:
    rows, cols = len(mat), len(mat[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            print(mat[top][i], end=' ')
        top += 1

        for i in range(top, bottom + 1):
            print(mat[i][right], end=' ')
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(mat[bottom][i], end=' ')
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(mat[i][left], end=' ')
            left += 1

# Usage
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
spiral_matrix_traversal(mat)

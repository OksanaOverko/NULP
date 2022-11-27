import numpy as np

matrix = np.array([[21, 2, 5, 1],
                   [7, 35, 40, 39],
                   [3, 5, 1, 42]])
print('Matrix:\n', matrix)


def unicValue(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    print("\nUnique elements found:")

    for i in range(rows):
        for j in range(cols):
            columns = matrix[:, j]
            colMax = np.max(columns)

            if (np.sum(columns) - (2 * colMax)) < 0 and matrix[i, j] == colMax:
                row = matrix[i]

                if j != 0:
                    leftMaxEl = np.max(row[0: j])
                    if leftMaxEl >= matrix[i, j]:
                        continue

                if (cols - (j + 1)) != 0:
                    rightMinEl = np.min(row[j + 1: cols])
                    if rightMinEl <= matrix[i, j]:
                        continue

                print(matrix[i, j], 'in', i, 'row and', j, 'column')


unicValue(matrix)

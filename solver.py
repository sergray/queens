def compute(rows, columns, max_queens_on_sight, initial_queens):
    field = [[0 for j in range(columns)] for i in range(rows)]
    for queen in initial_queens:
        x = queen['x']; y = queen['y']
        field[x][y] = 1
    added_queens = set()
    # naive solution without backtracking
    i = 0; j = 0
    while j < columns:
        if can_add(i, j, field, max_queens_on_sight):
            added_queens.add((i, j))
            field[i][j] = 1
        i += 1
        if i >= rows:
            i = 0
            j += 1
    # from pprint import pprint; pprint(field)
    return list(added_queens)


def can_add(x, y, field, max_queens_on_sight):
    return not field[x][y] and on_sight_count(x, y, field) <= max_queens_on_sight


def on_sight_count(x, y, field):
    """
    >>> on_sight_count(0, 0, [[1, 2], [3, 4]])
    9
    >>> on_sight_count(1, 0, [[1, 2], [3, 4]])
    8
    >>> on_sight_count(0, 1, [[1, 2], [3, 4]])
    7
    >>> on_sight_count(1, 1, [[1, 2], [3, 4]])
    6
    >>> on_sight_count(1, 1, [[0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]])
    4
    """
    rows = len(field)
    cols = len(field[0])
    count = 0
    # in a row
    count += sum(field[x]) - field[x][y]
    # in a column
    count += sum(field[i][y] for i in range(rows)) - field[x][y]
    # left-up
    i = x - 1; j = y - 1
    while i >= 0 and j >= 0:
        count += field[i][j]
        i -= 1; j -= 1
    # right-down
    i = x + 1; y = x + 1
    while i < rows and j < cols:
        count += field[i][j]
        i += 1; j += 1
    # left-down
    i = x + 1; j = y - 1
    while i < rows and j >= 0:
        count += field[i][j]
        i += 1; j -= 1
    # right-up
    i = x - 1; j = y + 1
    while i >= 0 and j < cols:
        count += field[i][j]
        i -= 1; j += 1
    return count

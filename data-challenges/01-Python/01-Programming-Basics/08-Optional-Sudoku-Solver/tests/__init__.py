def in_vs_out(input, output):
    for i, row in enumerate(input):
        for j, num in enumerate(row):
            if num != 0:
                num_solved = output[i][j]
                if num != num_solved:
                    error_msg = f'''
Solved grid differs from input grid at row {i} and column {j}, expected {num}, got {num_solved}
input grid:\n
{display_grid(input)}
output grid:
{display_grid(output)}
                    '''
                    return (False, error_msg)
    return (True, 'OK')

def display_grid(grid):
    out = ""
    for row in grid:
        out += "  ".join([str(num) for num in row])
        out += "\n"
    return out

VALID_SET = list(range(1, 10))

def valid_rows(grid):
    for i, row in enumerate(grid):
        if sorted(row) != VALID_SET:
            error_msg = f'Row {i} is not valid, expected one occurence within {VALID_SET}, got {row}.'
            return (False, error_msg)
    return (True, 'OK')

def valid_columns(grid):
    for j in range(0, 9):
        col = []
        for i in range(0, 9):
            col.append(grid[i][j])
        if sorted(col) != VALID_SET:
            error_msg = f'Column {j} is not valid, expected one occurence within {VALID_SET}, got {col}.'
            return (False, error_msg)
    return (True, 'OK')

def valid_boxes(grid):
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            square = []
            for i in range(0, 3):
                i += box_row
                for j in range(0, 3):
                    j += box_col
                    square.append(grid[i][j])
            if sorted(square) != VALID_SET:
                x = ['left', 'middle', 'right'][round(j/3)]
                y = ['top', 'middle', 'bottom'][round(i/3)]
                if x == y:
                    location = 'center'
                else:
                    location = f'{y}-{x}'
                error_msg = f'Square {location} is not valid, expected one occurrence within {VALID_SET}, got {square}.'
                return (False, error_msg)
    return (True, 'OK')

def checker(grid):
    if not valid_rows(grid)[0]:
        return valid_rows(grid)
        if not valid_columns(grid)[0]:
            return valid_columns(grid)
    return valid_boxes(grid)

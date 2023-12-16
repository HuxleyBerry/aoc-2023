def row_matches(grid, row1, row2):
    return grid[row1] == grid[row2]

def column_matches(grid, col1, col2):
    return all(grid[i][col1] == grid[i][col2] for i in range(len(grid)))

def group_by_row_or_column(grid, group_method):
    groups = []
    _range = range(len(grid)) if group_method == "row" else range(len(grid[0]))
    for i in _range:
        found_preexisting_group = False
        for group in groups:
            if (group_method == "row" and row_matches(grid, i, group[0])) or (group_method == "col" and column_matches(grid, i, group[0])):
                group.append(i)
                found_preexisting_group = True
                break
        if not found_preexisting_group:
            groups.append([i])
    groups_reformatted = [0 for i in _range]
    for i, group in enumerate(groups):
        for row_or_col in group:
            groups_reformatted[row_or_col] = i
    return groups_reformatted  

def check_if_axis(groups, size):
    for i in range(1, size):
        width = min(i, size-i)
        success = True
        for offset in range(1, width+1):
            left = i-offset
            right = i+offset-1
            if not groups[left] == groups[right]:
                success = False
                break
        if success:
            return i


with open("input.txt") as file:
    all_grids = [grid.split("\n") for grid in file.read().split("\n\n")]
    sum = 0
    for grid in all_grids:
        vertical = check_if_axis(group_by_row_or_column(grid,"col"), len(grid[0]))
        if vertical is not None:
            sum += vertical
        else:
            horizontal = check_if_axis(group_by_row_or_column(grid,"row"), len(grid))
            sum += 100*horizontal
    print(sum)
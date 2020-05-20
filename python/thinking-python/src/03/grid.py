def print_horizontal(columns_number):
    column = '- - - - + '
    print('+', column*columns_number)

def print_vertical(columns_number):
    wall = '        | '
    print('|', wall*columns_number)
    print('|', wall*columns_number)
    print('|', wall*columns_number)
    print('|', wall*columns_number)

def print_row(columns_number):
    print_vertical(columns_number)
    print_horizontal(columns_number)

def print_grid():
    print_horizontal(2)
    print_row(2)
    print_row(2)

print_grid()

def print_grid_four():
    print_horizontal(4)
    print_row(4)
    print_row(4)
    print_row(4)
    print_row(4)

print_grid_four()
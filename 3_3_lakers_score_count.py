first_quarter = [2, 2, 2, 1, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1]

def count_points(list, score_type):
    return list.count(score_type)
                      
print('Az ' + str(count_points(first_quarter, 3)) + ' pontos találatok száma: ' + str(count_points(first_quarter, 3)) + ' db.')


def print_number_of_three_pointers(quarter, three_pointers):
    print('A(z) ' + quarter + ' negyedben ' + str(three_pointers) + ' darab hárompontos dobás volt.')

print_number_of_three_pointers('első', count_points(first_quarter, 3))
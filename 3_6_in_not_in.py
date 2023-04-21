lakers_starters = ['L. James', 'A. Davis', 'D. Green', 'K. Caldwell-Pope', 'A. Caruso']

def print_starter(list, name):
    if name in list:
        print(name + ' benne van a kezdőcsapatban.')
    else:
        print(name + ' a cserepadon van.')


print_starter(lakers_starters, 'L. James')

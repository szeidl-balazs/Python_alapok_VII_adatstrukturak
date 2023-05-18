coordinates = ('47,29,56.29', '19,02,36.97')

def print_coordinates(place,data):
    print('A ' + place + ' a következő koordináták alatt található:')
    print('Északi szélesség ' + str(data[0][0:2]) + ' fok ' + str(data[0][3:5]) + ' perc ' + str(data[0][6:11]) + ' másodperc.')
    print('Keleti hosszúság ' + str(data[1][0:2]) + ' fok ' + str(data[1][3:5]) + ' perc ' + str(data[1][6:11]) + ' másodperc.')

print_coordinates('Lánchíd',coordinates)

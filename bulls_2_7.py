favorite_team = ['Armstrong, BJ', 'Cartwright, Bill (C)', 'Grant, Horace', 'Hodges, Craig', 
                 'Hopson, Dennis', 'Jordan, Michael (C)', 'King, Stacey', 'Levingston, Cliff',
                 '	Paxson, John', 'Perdue, Will', 'Pippen, Scottie', 'Williams, Scott']


def remove_injured_players(list, index):
    favorite_team = list
    favorite_team[index] = 'injured'
    print(favorite_team)

remove_injured_players(favorite_team, 2)

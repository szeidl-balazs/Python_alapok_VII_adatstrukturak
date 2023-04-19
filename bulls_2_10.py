favorite_team = ['Armstrong, BJ', 'Cartwright, Bill (C)', 'Grant, Horace', 'Hodges, Craig', 
                 'Hopson, Dennis', 'Jordan, Michael (C)', 'King, Stacey', 'Levingston, Cliff',
                 '	Paxson, John', 'Perdue, Will', 'Pippen, Scottie', 'Williams, Scott']

def remove_player(team, player):
    team.remove(player)
    print(team)

remove_player(favorite_team, 'Hopson, Dennis')

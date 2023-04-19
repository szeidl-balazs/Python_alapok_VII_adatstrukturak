favorite_team = ['Armstrong, BJ', 'Cartwright, Bill (C)', 'Grant, Horace', 'Hodges, Craig', 
                 'Hopson, Dennis', 'Jordan, Michael (C)', 'King, Stacey', 'Levingston, Cliff',
                 '	Paxson, John', 'Perdue, Will', 'Pippen, Scottie', 'Williams, Scott']

def add_new_player(team, player):
    team.append(player)
    print(team)

add_new_player(favorite_team, 'Kukoc')

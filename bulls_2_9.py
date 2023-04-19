favorite_team = ['Armstrong, BJ', 'Cartwright, Bill (C)', 'Grant, Horace', 'Hodges, Craig', 
                 'Hopson, Dennis', 'Jordan, Michael (C)', 'King, Stacey', 'Levingston, Cliff',
                 '	Paxson, John', 'Perdue, Will', 'Pippen, Scottie', 'Williams, Scott']

def add_captain(team, player, index):
    team.insert(index, player)
    print(team)

add_captain(favorite_team, "Jordan Michale (C)", 0)


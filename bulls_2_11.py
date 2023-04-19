favorite_team = ['Jordan, Michael (C)', 'Armstrong, BJ', 'Cartwright, Bill (C)', 'Grant, Horace', 'Hodges, Craig', 
                 'Hopson, Dennis', 'Jordan, Michael (C)', 'King, Stacey', 'Levingston, Cliff',
                 'Paxson, John', 'Perdue, Will', 'Pippen, Scottie', 'Williams, Scott']

def delete_player(team):
    del team[-2:]
    del team[0]
    print(team)

delete_player(favorite_team)
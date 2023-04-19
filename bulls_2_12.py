Chicago_bulls = ['Jordan, Michael (C)', 'Armstrong, BJ', 'Cartwright, Bill (C)', 'Grant, Horace', 'Hodges, Craig', 
                 'Hopson, Dennis', 'Jordan, Michael (C)', 'King, Stacey', 'Levingston, Cliff',
                 'Paxson, John', 'Perdue, Will', 'Pippen, Scottie', 'Williams, Scott']

Los_Angeles_lakers = ['Elden Campbell', 'Vlade Divac', 'Larry Drew', 'A. C. Green', 'Magic_Johnson', 'Sam Perkins', 'Byron Scott', 'Tony Smith', 'Terry Teagle', 'Irving Thomas', 'Mychal Thompson', 'James Worthy']


def transfer_player(our_team, rival_team, player_index):
    rival_team.append(our_team.pop(player_index))
    print(rival_team)
    print(our_team)

transfer_player(Chicago_bulls, Los_Angeles_lakers, 2)
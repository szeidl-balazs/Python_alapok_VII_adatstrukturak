lakers_players = (('A. Davis', 3), ('L. James', 23), ('D. Green', 14), ('K. Caldwell-Pope', 1), ('A. Caruso', 4), ('M. Morris', 88), ('J. Dudley', 10), ('K. Kuzma', 0), ('D. Howard', 39), ('R. Rondo', 9), ('Q. Cook', 28), ('J. McGee', 7), ('J. Smith', 21))

lakers_final_game = ((1, 2, 3), (1, 2, 23), (1, 2, 23), (1, 1, 1), (1, 1, 1), (1, 3, 14), (1, 2, 23), (1, 2, 9), (1, 2, 1), (1, 2, 3), (1, 2, 9), (1, 2, 3), (1, 2, 3), (1, 2, 23), (1, 1, 23), (2, 2, 9), (2, 3, 9), (2, 2, 23), (2, 3, 88), (2, 2, 4), (2, 2, 9), (2, 2, 9), (2, 2, 3), (2, 2, 1), (2, 1, 1), (2, 1, 3), (2, 1, 3), (2, 1, 3), (2, 2, 3), (2, 2, 1), (2, 2, 4), (2, 3, 1), (2, 3, 1), (3, 2, 23), (3, 3, 14), (3, 2, 23), (3, 2, 14), (3, 2, 1), (3, 2, 0), (3, 2, 23), (3, 3, 9), (3, 2, 23), (3, 3, 9), (4, 3, 14), (4, 2, 3), (4, 1, 3), (4, 1, 3), (4, 3, 23), (4, 2, 23), (4, 2, 23), (4, 2, 23), (4, 3, 39))


player_name = 'D. Green'
quarter = 3
score_type = 2

"""Converts name to jersey number:"""

def get_jersey_number(players, name):
    for player in players:
        if name in player:
            return player[1]

jersey_number = get_jersey_number(lakers_players, player_name)

"""Calculates the sum of scoures in a quarter:"""

def get_player_score_in_quarter(scores, quarter, jersey):
    
    sum = 0
    
    for score in scores:
        if quarter == score[0] and jersey == score[2]:
            sum += score[1]

    return sum

player_scores = get_player_score_in_quarter(lakers_final_game, quarter, jersey_number)


"""Counts the score_type in a quarter_"""

def get_score_type_count(scores, quarter, jersey, score_type):
    
    sum_of_count = []
    
    for score in scores:  
        if (quarter == score[0] and score_type == score[1] and jersey == score[2]):
            sum_of_count.append(score[1])
        

    return len(sum_of_count)

score_type_count = get_score_type_count(lakers_final_game, quarter, jersey_number, score_type)




def print_player_stat_in_quarter(name, quarter, player_scores, score_type, score_type_count):

    print(name + ' statisztikája a(z) ' + str(quarter) + '. negyedben:')
    if player_scores != 0:
        print('Elért pontok: ' + str(player_scores))
        print(str(score_type) + ' pontos dobások száma: ' + str(score_type_count))
    else:
        print('Nem ért el pontot a negyedben.')
    

print_player_stat_in_quarter(player_name, quarter, player_scores, score_type, score_type_count)

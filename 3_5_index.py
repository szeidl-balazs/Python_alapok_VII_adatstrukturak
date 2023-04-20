final_scores = [116, 124, 115, 102, 111, 106]

def get_min_score(list):
    return min(list)

def get_max_score(list):
    return max(list)

def get_game_number(list, number):
    return list.index(number)

def print_final_stat(min_score, max_score, min_index, max_index):
    print('A fináléban játszott mérkőzések közül a legalacsonyabb pontszámú a ' + str(min_index) + '. meccs volt ' + str(min_score) + ' ponttal.')
    print('A fináléban játszott mérkőzések közül a legmagasabb pontszámú a ' + str(max_index) + '. meccs volt ' + str(max_score) + ' ponttal.')

print_final_stat(get_min_score(final_scores), 
                 get_max_score(final_scores), 
                 get_game_number(final_scores, get_min_score(final_scores)),
                 get_game_number(final_scores, get_max_score(final_scores))
                 )
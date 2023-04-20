final_scores = [116, 124, 115, 102, 111, 106]

def get_min_score(list):
    return min(list)

def get_max_score(list):
    return max(list)

def print_final_stat(list):
    print('A fináléban játszott mérkőzések közül a legalacsonyabb pontszámú meccs eredménye: ' + str(get_min_score(list)) + '.')
    print(' fináléban játszott mérkőzések közül a legmagasabb pontszámú meccs eredménye: ' + str(get_max_score(list)) + '.')

print_final_stat(final_scores)
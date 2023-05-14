scores_this_season = [116, 124, 115, 102, 111, 106, 99, 90]

def sum_of_scores(scores):
    sum = 0
    for score in scores:        
        sum += score
    
    return sum



def calculate_average(sum_input, list):
    average = sum_input / len(list)
    print(sum_input, average)
    
    

calculate_average(sum_of_scores(scores_this_season), scores_this_season)

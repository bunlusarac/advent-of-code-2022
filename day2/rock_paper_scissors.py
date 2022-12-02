from functools import reduce

txt = open("input.txt","r")
mx = [row.split() for row in txt]
txt.close()

shape_to_idx = {'A': 0, 'X': 0, 'B': 1, 'Y': 1, 'C': 2, 'Z': 2}
intent_to_shape = {'X': -1, 'Y': 0, 'Z': 1}
pts = {'WIN': 6, 'DRAW': 3, 'LOSE': 0}
payoff_mx = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]

def score(row, part2=False):
    p1 = shape_to_idx[row[0]]
    p2 = determine([p1, row[1]]) if part2 else shape_to_idx[row[1]]
    
    payoff_to_score = lambda x: pts['WIN'] if x==1 else (pts['DRAW'] if x==0 else pts['LOSE'])
    shape_score = p2 + 1
    score = payoff_to_score(payoff_mx[p1][p2]) + shape_score
    return score 

def determine(row):
    [p1, shape] = row
    shape = intent_to_shape[shape]

    for i in range(len(payoff_mx[0])):
        if payoff_mx[p1][i] == shape:
            return i

total_score = reduce(lambda acc, row: acc + score(row, part2=True), mx, 0)
print(total_score)

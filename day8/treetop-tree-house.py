mx = []
txt = open("input.txt", "r")

mx = [list(map(lambda x: int(x), list(row.strip()))) for row in txt]
txt.close()

n_r, n_c = len(mx), len(mx[0])
vis = 0

for r in range(0, n_r):
    for c in range(0, n_c): 
        if r == 0 or c == 0 or r == n_r-1 or c == n_c-1: 
            vis +=1
        else:
            for pivot in [
                [mx[r][c] for r in range(r)],
                [mx[r][c] for r in range(r+1, n_r)],
                [mx[r][c] for c in range(c)],
                [mx[r][c] for c in range(c+1, n_c)]
            ]:
                if all(map(lambda x: x < mx[r][c], pivot)):
                    vis += 1
                    break

print(vis)

#part2
max_score = 0

for r in range(0, n_r):
    for c in range(0, n_c): 
        score = 1
        for pivot in [ #UDLR
            [mx[r][c] for r in range(r)][::-1],
            [mx[r][c] for r in range(r+1, n_r)],
            [mx[r][c] for c in range(c)][::-1],
            [mx[r][c] for c in range(c+1, n_c)]
        ]:
            distance = 0
            for el in pivot:
                distance += 1
                if not el < mx[r][c]: break 

            score *= distance
            
        if score > max_score: max_score = score

print(max_score)
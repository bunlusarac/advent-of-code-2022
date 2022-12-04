from functools import reduce

txt = open("input.txt", "r")

def inclusive_reducer(acc, txt):
    [[l1, u1], [l2, u2]] = [map(int, p) for p in map(lambda x: x.split("-"), txt.split(","))]
    return acc + (1 if (l1 <= l2 and u1 >= u2) or (l2 <= l1 and u2 >= u1) else 0) 

def overlap_reducer(acc, txt):
    [[l1, u1], [l2, u2]] = [map(int, p) for p in map(lambda x: x.split("-"), txt.split(","))]
    return acc + (1 if not (u2 < l1 or u1 < l2) else 0) 

#print(reduce(inclusive_reducer, txt, 0))
print(reduce(overlap_reducer, txt, 0))

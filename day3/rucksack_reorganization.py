from string import ascii_lowercase, ascii_uppercase
from functools import reduce

priority_lc = {v: k+1 for k, v in enumerate(ascii_lowercase)} 
priority_uc = {v: k+27 for k, v in enumerate(ascii_uppercase)}
item2pr = priority_lc | priority_uc

txt = open("input.txt","r")

#sum all compartment priorities
def compartment_priority_reducer(acc, bag):
    bag = bag.strip()
    length = len(bag)
    c1, c2 = set(bag[:length//2]), set(bag[length//2:])
    priority = sum(map(lambda i: item2pr[i], c1.intersection(c2)))
    return acc + priority

#pack bags in groups 
def group_reducer(acc, bag):
    bag = bag.strip()
    GROUP_SIZE = 3
    
    if acc[1] == GROUP_SIZE:
        return (acc[0] + [[bag]], 1)
    else:
        return (acc[0][:-1] + [acc[0][-1] + [bag]], acc[1] + 1)

#find badge of a group
badge_reducer = lambda acc, bag: set(bag).intersection(acc)

#sum all group badge priorities
group_priority_reducer = lambda acc, grp:  acc + item2pr[list(reduce(badge_reducer, grp))[0]]

#total_compartment_priority = reduce(compartment_priority_reducer, txt , 0)
grouped_bags, _ = reduce(group_reducer, txt, ([[]], 0))
total_group_priority = reduce(group_priority_reducer, grouped_bags, 0)
print(total_group_priority)

txt.close()

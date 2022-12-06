from functools import reduce

txt = open("input.txt","r")

N_STACKS = 9
REVERSE_ORDER=False
stacks = {i: [] for i in range(N_STACKS)}
idx = [4*i+1 for i in range(N_STACKS)]

def reducer(acc, ln):
    stack_line, stacks = acc
    if(ln.isspace() or ln[1].isnumeric()): return False, stacks

    if stack_line:
        row_items = enumerate(map(lambda i: ln[i], idx))
        stacks= [[c] + stacks[i] if c != ' ' else stacks[i] for i, c in row_items] 
        stack_line = True   
    else:
        amt, src, dest = map(lambda i: int(ln.split()[i]), [1, 3, 5])
        stacks[dest-1] = stacks[dest-1] + stacks[src-1][-amt:][:: -1 if REVERSE_ORDER else 1] 
        stacks[src-1] = stacks[src-1][:-amt] 
        stack_line = False

    return stack_line, stacks

_, stacks = reduce(reducer, txt, [True, stacks]) 
print(reduce(lambda acc, x: acc+str(x[-1]), stacks, ""))
txt.close()
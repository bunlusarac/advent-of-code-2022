from functools import reduce
txt = open("input.txt","r")

def reducer(acc, cal):
    if cal.strip():
        return acc[:-1] + [[acc[-1][0] + [cal], acc[-1][1] + int(cal)]]
    else:
        return acc + [[[], 0]]

elf_vector = reduce(reducer, txt, [[[], 0]])
txt.close()

elf_vector.sort(reverse=True, key=lambda t: t[1])
print(elf_vector[0][1])
print(reduce(lambda acc, x: acc + x[1], elf_vector[:3], 0))
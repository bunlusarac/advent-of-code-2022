from functools import cmp_to_key
from math import prod

txt = open("input.txt", "r")

packets = [eval(line) for line in txt if not line.isspace()]
ordered_pair_indices = []

def compare(p1, p2):
    if type(p1) is int and type(p2) is int:
        if p1 < p2:     return 1
        elif p1 > p2:   return -1
        else:           return 0
    else:
        p1 = [p1] if type(p1) is not list else p1
        p2 = [p2] if type(p2) is not list else p2
        l1, l2 = len(p1), len(p2)
        lmin = min(l1, l2)

        for i in range(lmin):
            cmpres = compare(p1[i], p2[i])

            if i == lmin - 1:
                if l1 == l2:
                    return cmpres
                elif lmin == l1:
                    if cmpres == 0: return 1
                    else:           return cmpres
                elif lmin == l2:
                    if cmpres == 0: return -1
                    else:           return cmpres
            else:
                if cmpres == 0: continue
                else:           return cmpres
            
        if l1 == l2: return 0
        else:
            if l1 == 0:     return 1
            elif l2 == 0:   return -1


for i in range(0, len(packets), 2):
    p1, p2 = packets[i:i+2]
    if compare(p1, p2) == 1: ordered_pair_indices.append(i//2 + 1)

print(sum(ordered_pair_indices))

divider_packets = [[[2]], [[6]]] 
organized_packets = divider_packets + packets
organized_packets = sorted(organized_packets, key=cmp_to_key(compare), reverse=True)
divider_packet_indices = [organized_packets.index(divider) + 1 for divider in divider_packets]
decoder_key = prod(divider_packet_indices)

print(decoder_key)
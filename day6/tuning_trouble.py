from functools import reduce

txt = open("input.txt","r")
stream = txt.read()

def find_signal(stream, slice_length=4):
    for i in range(len(stream) - slice_length):
        sig = stream[i:i+slice_length]
        if len(set(sig)) != slice_length: continue
        else: return i + slice_length, sig

print(find_signal(stream))
print(find_signal(stream, slice_length=14))
txt.close()
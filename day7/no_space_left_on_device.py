import re

txt = open("input.txt", "r")
fulltext = txt.read()

def tokenize(input):
    A = re.sub("[$] cd (\/|\w+)\n[$] ls\n", r"A \1\n", input)
    B = re.sub("[^c]([dir|\d+]+) ([a-zA-Z.]+)", r"\nB \1 \2", A)
    C = re.sub("[$] cd ..", r"C", B)

    return C

def browse(stack):
    temp = fs['content']
    ref = None


    for dest in stack:
        ref = temp[dest]
        temp = temp[dest]['content']
    
    return ref

fs = {'content': {}, 'size': 0}
stack = []
sizes = []

def parse(input):
    tokenized_lines = tokenize(input).splitlines()
    pwd = fs

    for line in tokenized_lines:
        tokens = line.split()
        token_type = tokens[0]

        if token_type == "A":
            node = tokens[1]
            stack.append(node)
            pwd['content'][node] = {'content': {}, 'size': 0}
            pwd = pwd['content'][node]
            

        elif token_type == "B":
            type_or_size, node = tokens[1:] 
            
            if type_or_size != "dir":
                pwd["content"][node] = {'size': int(type_or_size)}
            else:
                continue

        elif token_type == "C":
            for file in pwd['content'].values():
                pwd['size'] += file['size']
                
            sizes.append(pwd['size'])
            stack.pop()
            pwd = browse(stack)

    
    while len(stack) != 0:
        for file in pwd['content'].values():
            pwd['size'] += file['size']
            
        sizes.append(pwd['size'])
        stack.pop()
        pwd = browse(stack) 

parse(fulltext)
total_pt1 = sum(filter(lambda x: x < 100000, sizes))
print(total_pt1)

disk_space = 70000000
used_space = fs['content']['/']['size']
remaining_space = disk_space - used_space
update_space = 30000000
deleted_space = update_space - remaining_space


min_dir = {'content':{}, 'size': disk_space}
min_size = disk_space

def scan(pwd):
    global min_size

    for _, dir in pwd['content'].items():
        if 'content' in dir.keys() and dir['size'] >= deleted_space :
            min_size = min(scan(dir)['size'], min_size)

    return pwd
deleted_dir = scan(fs)
print(min_size)

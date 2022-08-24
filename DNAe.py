from re import X
import sys

original_sequences = []
print(" ")

with open(sys.argv[1], 'r') as file: #
    for line in file:
        line = line.rstrip()
        original_sequences.append(line)

max_pairs = int(original_sequences[0])


pair_count = 0
while pair_count <= max_pairs - 1:
    pair_count += 1
    seq1 = original_sequences[pair_count * 2 - 1]
    seq2 = original_sequences[pair_count * 2]

    segments1 = {}
    segments2 = {}

    size = 2
    sequence_length = len(seq1)

    while size <= sequence_length:
        
        segments1[size] = []
        x = 0
        while (x + size) <= sequence_length:
            segments1[size].append(seq1[x:x+size])
            x += 1
        size += 1

    size = 2
    sequence_length = len(seq2)

    while size <= sequence_length:
        
        segments2[size] = []
        x = 0
        while (x + size) <= sequence_length:
            segments2[size].append(seq2[x:x+size])
            x += 1
        size += 1

    size = 2
    max_size = min(len(segments1), len(segments2)) + 1
    match = ''
    final_pairs = []
    final_pair_size = 0
    while size <= max_size:
        for x in segments1[size]:
            for y in segments2[size]:
                if x == y:
                    final_pairs.append(x)
                    final_pair_size = size
        size += 1
    if len(final_pairs) == 0:
        print("No Common Sequence Found.")
    else:
        final_pairs.sort()
        for segment in final_pairs:
            if len(segment) == final_pair_size:
                print(segment)
    print(" ")
 
    

with open("rosalind_gc.txt") as file:
    seq = file.read().split(">")[1:]

    seq_id_list = []
    seq_only_list = []

    for s in seq:
        seq_lines = s.split('\n')
        seq_only = ''.join(seq_lines[1:])
        seq_id = seq_lines[0]
        seq_only_list.append(seq_only)
        seq_id_list.append(seq_id)

def gc_cal(seq):
    length = len(seq)
    gc_count = 0
    for s in seq:
        if s == 'G':
            gc_count += 1
        elif s == 'C':
            gc_count += 1
    gc = (gc_count / length) * 100
    return "{:.6f}".format(gc)

gc_list = []
for seq in seq_only_list:
    result = gc_cal(seq)
    gc_list.append(result)

max_index = gc_list.index(max(gc_list))


# print(seq_only_list)
# print(max_index)
# print(gc_list)

print(seq_id_list[max_index])
print(gc_list[max_index])

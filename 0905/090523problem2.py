def problem2(dna_string):
    new = ''
    for n in dna_string:
        if n == 'T':
            new += 'U'
        else:
            new += n
    return new

with open("rosalind_rna.txt") as file:
    seq = file.readline().rstrip("\n")
    print(problem2(seq))

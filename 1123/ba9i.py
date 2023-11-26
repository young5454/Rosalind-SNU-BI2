# Burrows-Wheeler Transform of a string

def cyclic_rotations(seq):
    n = len(seq)
    cycles = []

    for i in range(n):
        curr = seq[i:] + seq[:i]
        cycles.append(curr)
    
    cycles.sort()
    
    return cycles


def get_bwt(cycles):
    # Return the Burrows-Wheeler transform using cycles
    bwt = ''
    for seq in cycles:
        end_letter = seq[-1]
        bwt += end_letter
    
    return bwt


if __name__ == '__main__':
    with open("rosalind_ba9i.txt") as file:
        seq = file.readline()

        cycles = cyclic_rotations(seq)
        for c in cycles:
            print(c)
        print()
        
        bwt = get_bwt(cycles)
        print(bwt)
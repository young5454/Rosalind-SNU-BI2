# String from its Burrows-Wheeler Transform

def inverse_bwt(bwt):
    # Initiate front and last column
    front = sorted(bwt)
    last_column = list(bwt)

    n = len(bwt)
    counter = 1

    while counter < n:
        composition = []
        for i in range(n):
            composition.append(last_column[i] + front[i])
        
        composition.sort()
        front = composition

        counter += 1
    
    first = front[0]
    # Move $ to last
    original = first[1:] + first[0]
    
    return original, front


if __name__ == '__main__':
    with open("rosalind_ba9j.txt") as file:
        bwt = file.readline()

        original = inverse_bwt(bwt)[0]
        print(original)
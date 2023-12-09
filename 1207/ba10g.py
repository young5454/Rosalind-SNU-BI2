# Sequence Alignment with Profile HMM Problem
from ba10e import check_position
from ba10f import profile_hmm_with_pseudo

if __name__ == '__main__':
    with open("rosalind_ba10g.txt") as file:
        # Text
        text = file.readline().strip()

        _ = file.readline().strip()
        
        # Theta value and pseudocount
        theta, pseudocount = file.readline().split()
        theta = float(theta)
        pseudocount = float(pseudocount)

        _ = file.readline().strip()

        # Sigma
        sigma = file.readline().split()

        _ = file.readline().strip()

        # Alignments
        alignments = file.read().split('\n')

        checklist, profile = check_position(alignments, theta)

        for f in profile:
            print(f)
        
        emission, transition = profile_hmm_with_pseudo(alignments, checklist, profile, sigma, pseudocount)
        for t in transition:
            print(t)
        print('--------')
        for e in emission:
            print(e)
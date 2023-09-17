def problem1(dna_string):
    nucleotides = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for n in dna_string:
        curr = nucleotides[n] 
        curr += 1
        nucleotides[n] = curr
    print(nucleotides['A'], nucleotides['C'], nucleotides['G'], nucleotides['T'])


dataset = 'ATTTATGTCGACAAACGGATTTACTGCACAGTACACTTGCACAGATGGGAAACAGCGTTAAAGCAGACGTCTCTACTGCGACGAGATACGTCTCACGTTCATTCCAGACCCCGTGAAGGGGTCATGAATACATGGTCGAGAGTGTGGCAACGTGTCTAGCATGGCGTCCCGGGTAGTTACATAATTACGACAAGCGCTGGCCGACGGGCGGCGAGCGACTCGTGGGATACAAGGGTAAATAGTGCGGCCCGTGGAAATGTTTAGGTCACTACCCGGTCTTTTCCGCCACGGTTACCGAAATAGATAATAGCACGAGTAGCGATCCTTGTCAAGATGTTTCCTCAAACGATCGAAATGAAATCAATATTAAGGAACGGGCGATCCTACTCTTAGGTGATTAAAGACTCTCAAATAGCCCGCACCTCGAGACCAGTCGATACCGGGCCGAACGCGGGCCTTTCTATGGGAAATCTTGTTGCGGAAAGTCTGGACTGTAATGACACCATTCGTATGAGGGATTATATGCCCACAAGCGGAACATCATGTTATGGGGATGAGACACGGACCGTGGAAATGTAGCCTTGAAAGGTACGACTCGGAAACCGCTCACTGATACAAGATCATTGCGTCTACACTCATAACACAAGCAGTCAGAGCCCAGAGAAGAGCTCAAGTTAGATTTCTGTTCTGAATGGATTCATCACCTCATGGCGGACGCCATGTCTCTATGTCCATTATCGCGAGCCAGAGCCCCACCATATACGCCGGAGCTCGGTTGGTAAGCCGCAGCTATGGTGCTGCAACTCCGATAGCTCGATCGAGTATGATACGGATGATACGCCTGAAGGTGCATCAGGTCTTTTAATTGATCCATCCCCTCTGTGAGGACACGGCAATCGGCAATTTAATCGTGTCTCTGACCGGTTTGGGTTGGTGCCAACGGTCGTG'
problem1(dataset)
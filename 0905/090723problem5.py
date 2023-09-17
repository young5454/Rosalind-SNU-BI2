with open("rosalind_ba1b.txt") as file:
    text = file.readline().strip('\n')
    k = int(file.readline().strip('\n'))

def kmer(text, i, k):
    mer = text[i:i+k]
    return mer

def freqeuncy_table(text, k):
    freqMap = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = kmer(text, i, k)
        if pattern not in freqMap:
            freqMap[pattern] = 1
        else:
            freqMap[pattern] = freqMap[pattern] + 1
    return freqMap


def max_map(freqMap):
    return max(freqMap.values())

def better_frequent_words(text, k):
    freq_patterns = []
    freqMap = freqeuncy_table(text, k)
    for pattern in freqMap.keys():
        if freqMap[pattern] == max_map(freqMap):
            freq_patterns.append(pattern)
    
    output = ' '.join(freq_patterns)
    print(output)

better_frequent_words(text, k)
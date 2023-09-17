with open("rosalind_ba1a.txt") as file:
    text = file.readline().strip('\n')
    pattern = file.readline().strip('\n')

def PatternCount(text, pattern):
    count = 0
    text_length = len(text)
    pattern_length = len(pattern)
    for i in range(text_length - pattern_length + 1):
        if text[i:i + pattern_length] == pattern:
            count += 1
    return count

print(len(text))
print(pattern)
print(PatternCount(text, pattern))

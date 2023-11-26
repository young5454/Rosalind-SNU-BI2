from ba9g import generate_suffix_array


def pattern_finding(pattern, seq, suffix_array):
    match = []
    n = len(seq)

    # Perform binary search to find the range of suffixes starting with 'pattern'
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        suffix = seq[suffix_array[mid]:]

        # Match
        if suffix.startswith(pattern):
            match.append(suffix_array[mid])
            # Left search
            left = mid - 1
            while left >= 0:
                if seq[suffix_array[left]:].startswith(pattern):
                    match.append(suffix_array[left])
                left -= 1

            # Right search
            right = mid + 1
            while right < n:
                if seq[suffix_array[right]:].startswith(pattern):
                    match.append(suffix_array[right])
                right += 1

            return sorted(match)
        
        elif pattern < suffix:
            high = mid - 1

        else:
            low = mid + 1

    return match


if __name__ == '__main__':
    with open("rosalind_ba9h.txt") as file:
        data_list = file.read().splitlines()

        seq = data_list[0]
        seq = seq + '$'
        patterns = data_list[1:]

        suffix_array = generate_suffix_array(seq)

        total_matches = []
        for pattern in patterns:
            match = pattern_finding(pattern, seq, suffix_array)
            total_matches += match

        # Int list to string list
        total_matches = sorted(total_matches)
        total_matches = [str(t) for t in total_matches]

        # Print results
        result = ' '.join(total_matches)
        print(result)

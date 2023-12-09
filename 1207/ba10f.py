# Construct a Profile HMM
import numpy as np

def check_position(alignments, theta):
    # Length of each alignment
    n = len(alignments[0])
    num_of_alignments = len(alignments)

    # Check type of each position
    checklist = []

    for i in range(n):
        tmp_count = 0
        for ali in alignments:
            if ali[i] == '-':
                tmp_count += 1
        if (tmp_count / num_of_alignments) > theta:
            checklist.append('i')
        elif tmp_count == 0:
            checklist.append('h')
        else:
            checklist.append('d')
        
    # Initialize and create profile
    profile = [[] * p for p in range(num_of_alignments)]
    
    for i in range(n):
        for j in range(num_of_alignments):
            ali = alignments[j]
            if checklist[i] == 'd':
                profile[j].append({'del': ali[i]})
            elif checklist[i] == 'i':
                # Check if insertion is sequential
                if i > 0 and checklist[i-1] == 'i':
                    ins_dic = profile[j][-1]
                    tmp = ins_dic['ins'] 
                    ins_dic['ins'] = tmp + ali[i]
                else:
                    profile[j].append({'ins': ali[i]})
            else:
                profile[j].append({'hid': ali[i]})

    return checklist, profile


def profile_hmm_with_pseudo(alignments, checklist, profile, sigma, pseudocount):
    # Number of alignments
    num_of_alignments = len(alignments)

    # Number of M: hidden + deletion
    num_of_m = checklist.count('h') + checklist.count('d')

    # Number of rows: Start + I0 + (Number of M) x 3 + End
    # Order: S, I0, (M, D, I), E
    num_of_rows = 3 + num_of_m * 3 

    # Make candidates
    m_candidates = []
    i_candidates = ['I0']
    d_candidates = []
    for i in range(num_of_m):
        m_candidates.append('M' + str(i+1))
        i_candidates.append('I' + str(i+1))
        d_candidates.append('D' + str(i+1))

    # Number of columns: length of sigma
    num_of_cols = len(sigma)

    # Emission matrix
    emission = np.zeros((num_of_rows, num_of_cols))

    # New checklist: considering the sequential insertions
    new_checklist = []
    for a in range(len(profile[0])):
        new_checklist.append(list(profile[0][a].keys())[0][0])
    print(new_checklist)

    ins_index = []
    for i in range(len(new_checklist)):
        if new_checklist[i] == 'i':
            ins_index.append(i)
    
    ins_dic = {}
    for i in ins_index:
        tmp = ''
        for item in profile:
            # Concatenate all the alphabets and -s
            tmp += item[i]['ins']

            # Calculate probability
            ins_counted = []
            for s in sigma:
                if len(tmp) - tmp.count('-') == 0:
                    ins_counted.append(0)
                else:
                    ins_counted.append(tmp.count(s) / (len(tmp) - tmp.count('-')))

        # Check how many h and d occurred before
        ins_numbering = new_checklist[:i].count('h') + new_checklist[:i].count('d')
        key = 'I' + str(ins_numbering)
        
        # Consider Pseudocounts
        divider = 1 + len(ins_counted) * pseudocount
        ins_counted_pseudocount = [(x + pseudocount) / divider for x in ins_counted]
        ins_dic[key] = ins_counted_pseudocount
    
    print(ins_dic)

    # Get hidden node indices and probabilities
    hid_index = []
    for i in range(len(new_checklist)):
        if new_checklist[i] == 'h':
            hid_index.append(i)

    hid_dic = {}
    for h in hid_index:
        tmp = []
        for item in profile:
            # Append only the alphabet
            tmp.append(item[h]['hid'])

            # Calculate probability
            hid_counted = []
            for s in sigma:
                hid_counted.append(tmp.count(s) / (num_of_alignments - tmp.count('-')))

        # Check how many h and d occurred before
        num_of_h_and_d = new_checklist[:h].count('h') + new_checklist[:h].count('d') + 1
        key = 'M' + str(num_of_h_and_d)
        hid_dic[key] = hid_counted

        # Consider Pseudocounts
        divider = 1 + len(hid_counted) * pseudocount
        hid_counted_pseudocount = [(x + pseudocount) / divider for x in hid_counted]
        hid_dic[key] = hid_counted_pseudocount

    print(hid_dic)

    # Get deletion node indices and probabilities
    del_index = []
    for i in range(len(new_checklist)):
        if new_checklist[i] == 'd':
            del_index.append(i)
    
    del_dic = {}
    for d in del_index:
        tmp = []
        for item in profile:
            # Append only the alphabet
            tmp.append(item[d]['del'])

            # Calculate probability
            del_counted = []
            for s in sigma:
                del_counted.append(tmp.count(s)/ (num_of_alignments - tmp.count('-')))

        # Check how many h and d occurred before
        num_of_h_and_d = new_checklist[:d].count('h') + new_checklist[:d].count('d') + 1
        key = 'M' + str(num_of_h_and_d)

        # Consider Pseudocounts
        divider = 1 + len(del_counted) * pseudocount
        del_counted_pseudocount = [(x + pseudocount) / divider for x in del_counted]
        del_dic[key] = del_counted_pseudocount
        
    print(del_dic)

    # Define all_dic to save all entries
    all_dic_emission = {}

    # Add S
    all_dic_emission['S'] = list(np.zeros(num_of_cols))

    # Add I0 
    if 'I0' in ins_dic.keys():
        all_dic_emission['I0'] = ins_dic['I0']
    else:
        # Consider Pseudocount
        zeros = list(np.zeros(num_of_cols))
        divider = len(zeros) * pseudocount
        pseudocount_considered = [(x + pseudocount) / divider for x in zeros]
        all_dic_emission['I0'] = pseudocount_considered

    # Add M, D, I 
    for k in range(num_of_m):
        m = 'M' + str(k+1)
        d = 'D' + str(k+1)
        i = 'I' + str(k+1)

        # M
        if m in hid_dic.keys():
            all_dic_emission[m] = hid_dic[m]
        elif m in del_dic.keys():
            all_dic_emission[m] = del_dic[m]
        else:
            # Consider Pseudocount
            zeros = list(np.zeros(num_of_cols))
            divider = 1 + len(zeros) * pseudocount
            pseudocount_considered = [(x + pseudocount) / divider for x in zeros]
            all_dic_emission[m] = pseudocount_considered
        
        # D
        all_dic_emission[d] = list(np.zeros(num_of_cols))

        # I
        if i in ins_dic.keys():
            all_dic_emission[i] = ins_dic[i]
        else:
            # Consider Pseudocount
            zeros = list(np.zeros(num_of_cols))
            divider = len(zeros) * pseudocount
            pseudocount_considered = [(x + pseudocount) / divider for x in zeros]
            all_dic_emission[i] = pseudocount_considered
    
    # Add E
    all_dic_emission['E'] = list(np.zeros(num_of_cols))

    # Format to print
    header = ' ' + ' '.join(sigma)
    emission = [header]

    for element in all_dic_emission.items():
        # Change to string list
        stringed = []
        for p in element[1]:
            if p == 0: stringed.append('0.0')
            else: stringed.append(str(p))
        row = element[0] + ' ' + ' '.join(stringed)
        emission.append(row)

    # Transition
    # Make new profile with M, D, I symbols
    new_profile = [[] * p for p in range(num_of_alignments)]
    n = len(profile[0])

    hh, dd, ii = 0, 0, 0
    hid_dic_keys, del_dic_keys, ins_dic_keys = list(hid_dic.keys()), list(del_dic.keys()), list(ins_dic.keys())

    for i in range(n):
        for j in range(num_of_alignments):
            curr = profile[j][i]
            if 'hid' == list(curr.keys())[0]:
                hh = hid_index.index(i)
                new_key = hid_dic_keys[hh]
                new_profile[j].append({new_key: list(curr.values())[0]})

            elif 'del' == list(curr.keys())[0]:
                dd = del_index.index(i)
                if list(curr.values())[0] == '-':
                    # M to D
                    new_key = 'D' + del_dic_keys[dd][1]
                    new_profile[j].append({new_key: list(curr.values())[0]})
                else:
                    new_key = del_dic_keys[dd]
                    new_profile[j].append({new_key: list(curr.values())[0]})

            elif 'ins' == list(curr.keys())[0]:
                ii = ins_index.index(i)
                new_key = ins_dic_keys[ii]
                new_profile[j].append({new_key: list(curr.values())[0]})

    for n in new_profile:
        print(n)
    
    # Iterate pairs
    n = len(profile[0])
    pair_list = []

    # Consider S -> first
    tmp = {'S': []}
    for j in range(num_of_alignments):
        next = list(new_profile[j][0].keys())[0]
        tmp['S'].append(next)
    pair_list.append(tmp)

    # Middle nodes
    for p in range(n-1):
        tmp = {}
        for j in range(num_of_alignments):
            curr = list(new_profile[j][p].keys())[0]

            next = list(new_profile[j][p+1].keys())[0]
            if curr not in tmp.keys():
                tmp[curr] = [next]
            else:
                tmp[curr].append(next)

        pair_list.append(tmp)
    
    # Consider last -> E
    tmp = {}
    for j in range(num_of_alignments):
        curr = list(new_profile[j][n-1].keys())[0]
        if curr not in tmp.keys():
            tmp[curr] = ['E']
        else:
            tmp[curr].append('E')
    pair_list.append(tmp)
    
    kag = {}
    for pair in pair_list:
        for elem in pair.items():
            key, value = elem
            set_value = set(value)
            tmp = []
            for s in set_value:
                # Consider Pseudocount
                tmp.append([s, list(value).count(s) / len(value)])
                kag[key] = tmp
    
    # Finalize transition matrix
    all_dic_transition = {}
    candidates = list(all_dic_emission.keys())

    for c in candidates:
        template = {key: 0 for key in list(all_dic_emission.keys())}
        if c in kag.keys():
            for kg in kag[c]:
                neighbor = kg[0]
                template[neighbor] = kg[1]
                all_dic_transition[c] = template
    
    print(all_dic_transition)

    # Format to print
    header = ' ' + ' '.join(candidates)
    transition = [header]
    zeros = ['0.0'] * len(candidates)
    for key in candidates:
        if key in list(all_dic_transition.keys()):
            value = all_dic_transition[key]
            listy = list(value.values())
            stringed = []
            for l in listy: 
                if l == 0:
                    stringed.append('0.0')
                else:
                    stringed.append(str(l))
            row = key + ' ' + ' '.join(stringed)
            transition.append(row)
        else:
            row = key + ' ' + ' '.join(zeros)
            transition.append(row)

    return emission, transition


if __name__ == '__main__':
    with open("rosalind_ba10f.txt") as file:
        # Theta value
        theta, pseudocount = file.readline().split()
        theta = float(theta)
        pseudocount = float(pseudocount)

        _ = file.readline().strip()

        # Sigma
        sigma = file.readline().split()

        _ = file.readline().strip()

        # Alignments
        alignments = file.read().split('\n')
        # print(alignments)

        checklist, profile = check_position(alignments, theta)

        for f in profile:
            print(f)
        
        emission, transition = profile_hmm_with_pseudo(alignments, checklist, profile, sigma, pseudocount)
        for t in transition:
            print(t)
        print('--------')
        for e in emission:
            print(e)
        

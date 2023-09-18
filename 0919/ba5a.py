
# def DPChange(money, coins):


if __name__ == '__main__':
    with open("rosalind_ba5a.txt") as file:
        data_list = []
        for line in file:
            cleaned_line = line.strip()
            data_list.append(cleaned_line)
        money = int(data_list[0])
        coins = data_list[1].split(',')

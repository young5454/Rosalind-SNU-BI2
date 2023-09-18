
def DPChange(money, coins):
    min_num_coins = [0] * (money + 1)
    for m in range(1, money + 1):
        min_num_coins[m] = float('inf')
        for i in range(len(coins)):
            if m >= coins[i]:
                if min_num_coins[(m - coins[i])] + 1 < min_num_coins[m]:
                    min_num_coins[m] = min_num_coins[(m - coins[i])] + 1
    return min_num_coins[money]


if __name__ == '__main__':
    with open("rosalind_ba5a.txt") as file:
        data_list = []
        for line in file:
            cleaned_line = line.strip()
            data_list.append(cleaned_line)
        money = int(data_list[0])
        coins = data_list[1].split(',')
        coins = [int(c) for c in coins]
        print(DPChange(money, coins))

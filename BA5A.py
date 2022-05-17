def dpChangeMoney(money, coins):
    minnumcoins = (money + 1) * [0]
    for m in range(1, money + 1):
        minnumcoins[m] = m + 1 
        for coin in coins:
            if m >= coin:
                if minnumcoins[m - coin] + 1 < minnumcoins[m]:
                    minnumcoins[m] = minnumcoins[m - coin] + 1
    return minnumcoins[money]

with open('/content/rosalind_ba5a.txt') as f:
  input = [x.rstrip() for x in f.readlines()]
money = int(input[0])
coins = [int(x) for x in input[1].split(",")]

dpChangeMoney(money, coins)


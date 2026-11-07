
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    coin_dict = {}
    for coin in coins:
        count = amount // coin
        amount = amount % coin
        if count > 0:
            coin_dict[coin] = count
    return coin_dict

print(find_coins_greedy(113))


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    last_coin = [0] * (amount + 1)
    
    for x in range(1, amount + 1):
        for coin in coins:
            if coin <= x:
                candidate = 1 + min_coins[x - coin]
                if candidate < min_coins[x]:
                    min_coins[x] = candidate
                    last_coin[x] = coin

    result = {}
    x = amount
    while x > 0:
        coin = last_coin[x]
        if coin not in result:
            result[coin] = 0
        result[coin] += 1
        x = x - coin
    return result

print(find_min_coins(113))
import timeit


def find_min_coins(sum, coins):
    min_coins_required = [0] + [float('inf')] * sum
    coin_used = [0] * (sum + 1)

    for i in range(1, sum + 1):
        for coin in coins:
            print(f"--- sub_sum={i}, coin={coin} ---")
            if i >= coin and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1
                coin_used[i] = coin
            print(f"Min coins required table: \t{min_coins_required}")
            print(f"Coin used table: \t\t{coin_used}")

    coins_count = {}

    current_sum = sum
    # 12
    while current_sum > 0:
        coin = coin_used[current_sum]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        current_sum -= coin

    coins_count_ordered = {coin: coins_count.get(coin, 0) for coin in coins if coin in coins_count}
    return coins_count_ordered, coin_used


if __name__ == '__main__':
    cases = [([50, 25, 10, 5, 2, 1], 137),
             ([10, 6, 1], 12)
             ]
    
    functions = [find_min_coins]

    for coins, cash_amount in cases:
        print(f"\n\tCase for {coins} and sum: {cash_amount}")
        for fun in functions:
            time = timeit.timeit(lambda: fun(cash_amount, coins), number=1)
            result, coin_used = fun(cash_amount, coins)
            print("Result for sum {}: {}".format(fun.__name__, result))

            print("\tShow calculated table of best coins for each amount")
            for calculated_sum, best_coin in enumerate(coin_used):
                print(f"Best coin to use for {calculated_sum} is {best_coin}")

            print("\tShow how best result was calculated")
            current_sum = cash_amount
            while current_sum > 0:
                print(f"Current sum is {current_sum}")
                coin = coin_used[current_sum]
                print(f"Found that for the sum {current_sum} the best coin to use is {coin}")
                current_sum -= coin
                print("Calculating next value of sum to search...")

            print("Time taken for {}: {:.6f} seconds".format(fun.__name__, time))


#                                 12
#                                [10, 6, 1]
# sub_sum                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Min coins required table:       [0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 1,  2,  inf]
# Coin used table:                [0, 1, 1, 1, 1, 1, 6, 6, 6, 6, 10, 10, 10]

# 12        10
# sub_sum >= coin
# Min coins required table[sub_sum - coin] + 1 (#10) = 3

# if (Min coins required table[sub_sum - coin] + 1 < Min coins required table[sub_sum])
#    coin used[sub_sum] = coin

            

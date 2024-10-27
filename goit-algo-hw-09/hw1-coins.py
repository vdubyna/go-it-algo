import time
import random

def find_coins_greedy(amount, coins):
    result = {}
    for coin in sorted(coins, reverse=True):
        count = amount // coin
        if count != 0:
            result[coin] = count
        amount %= coin
    return result

def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    result = {}
    while amount > 0:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                amount -= coin
                break
    return result

def compare_algorithms_quality(num_cases, coins):
    random_amounts = [random.randint(100, 500) for _ in range(num_cases)]
    results = []

    for amount in random_amounts:
        greedy_result = find_coins_greedy(amount, coins)
        dp_result = find_min_coins(amount, coins)

        if sum(dp_result.values()) < sum(greedy_result.values()):
            results.append({
                "Amount": amount,
                "Greedy Coins": sum(greedy_result.values()),
                "DP Coins": sum(dp_result.values()),
                "Greedy Distribution": greedy_result,
                "DP Distribution": dp_result
            })

    # Print results as a table
    if results:
        print(f"{'Amount':>7} {'Greedy Coins':>12} {'DP Coins':>10} {'Greedy Distribution':>20} {'DP Distribution':>20}")
        for result in results:
            print(f"{result['Amount']:>7} {result['Greedy Coins']:>12} {result['DP Coins']:>10} {str(result['Greedy Distribution']):>20} {str(result['DP Distribution']):>20}")
    else:
        print("No cases where DP outperforms Greedy in terms of fewer coins used.")

def compare_algorithms_performance(coins, amounts):
    print(f"{'Amount':>7} {'Greedy Time':>12} {'DP Time':>10} {'Greedy Coins':>12} {'DP Coins':>10}")
    for amount in amounts:
        start_time = time.time()
        greedy_result = find_coins_greedy(amount, coins)
        greedy_time = time.time() - start_time

        start_time = time.time()
        dp_result = find_min_coins(amount, coins)
        dp_time = time.time() - start_time

        print(f"{amount:>7} {greedy_time:12.6f} {dp_time:10.6f} {sum(greedy_result.values()):>12} {sum(dp_result.values()):>10}")

# Define coin sets
coin_sets = [
    [50, 25, 10, 5, 2, 1],
    [1, 3, 4]
]

# Test performance for each coin set
for coins in coin_sets:
    print(f"\nTesting with coins: {coins}")
    test_amounts = [10, 50, 100, 200, 500, 1000, 2000]

    print(f"Test quality of performance")
    compare_algorithms_performance(coins, test_amounts)

    print(f"Test quality of algorithms")
    compare_algorithms_quality(20, coins)
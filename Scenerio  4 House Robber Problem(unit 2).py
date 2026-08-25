def house_robber(houses):
    if not houses:
        return 0

    if len(houses) == 1:
        return houses[0]

    dp = [0] * len(houses)

    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    return dp[-1]


houses = list(map(int, input("Enter house amounts: ").split()))

result = house_robber(houses)

print("Maximum amount:", result)
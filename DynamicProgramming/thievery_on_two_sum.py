# programmers

# 40 score (of 100)
import collections
def solution1(money):
    if not money:
        return 0
    money_count = len(money)
    if money_count <= 2:
        return max(money)
    dp = collections.OrderedDict()
    dp[0], dp[1] = money[0],  max(money[0], money[1])
    for i in range(2, money_count):
        if dp[i -1] > dp[i - 2] + money[i]:
            dp[i] = dp[i -1]
        else:
            dp[i] = dp[i - 2] + money[i]
    return dp.popitem()[1]


# 100 score (of 100)
def solution2(money):
    x1, y1, z1 = money[0], money[1], money[0]+money[2]
    x2, y2, z2 = 0, money[1], money[2]
    for i in money[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
    return max(x1, y1, y2, z2)

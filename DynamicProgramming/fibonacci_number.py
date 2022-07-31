import collections


class Solution1:
    dic = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if self.dic[n]:
            return self.dic[n]
        self.dic[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dic[n]

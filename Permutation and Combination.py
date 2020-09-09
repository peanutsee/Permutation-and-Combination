from math import factorial


class PnC:
    def __init__(self):
        pass

    def combination(self, n, r):
        return factorial(n)/(factorial(r) * factorial(n - r))

    def permutation(self, n, r):
        return self.combination(n, r) * factorial(r)

    def circular_permutation(self, n):
        return factorial(n - 1)
    
    

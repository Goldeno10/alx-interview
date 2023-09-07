#!/usr/bin/python3
"""
Task:
    Maria and Ben are playing a game. Given a set of consecutive
    integers starting from 1 up to and including n, they take turns
    choosing a prime number from the set and removing that number and
    its multiples from the set. The player that cannot make a move
    loses the game.
    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.

    Prototype: def isWinner(x, nums)
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
    Example:

    x = 3, nums = [4, 5, 1]
    First round: 4

    Maria picks 2 and removes 2, 4, leaving 1, 3
    Ben picks 3 and removes 3, leaving 1
    Ben wins because there are no prime numbers left for Maria to choose
    Second round: 5

    Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    Ben picks 3 and removes 3, leaving 1, 5
    Maria picks 5 and removes 5, leaving 1
    Maria wins because there are no prime numbers left for Ben to choose
    Third round: 1

    Ben wins because there are no prime numbers for Maria to choose
    Result: Ben has the most wins
"""


def isWinner(x, nums):
    """Determine who the winner of each game is."""
    def sieve(n):
        """Sieve of Eratosthenes."""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = [i for i in range(2, n + 1) if is_prime[i]]
        return primes

    def canWin(n, primes):
        """Determine if a player can win."""
        if n <= 1:
            return False
        for prime in primes:
            if n % prime == 0:
                return True
        return False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = sieve(n)
        maria_turn = True

        while n > 0:
            if canWin(n, primes):
                for prime in primes:
                    if n % prime == 0:
                        n -= prime
                        break
            else:
                break

            maria_turn = not maria_turn

        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

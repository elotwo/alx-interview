#!/usr/bin/python3
"""
Prime Game Winner
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    x: The number of rounds.
    nums: List of integers representing the highest number in each round.

    Returns:
    The name of the player that won the most rounds (either "Maria" or "Ben").
    If the winner cannot be determined, return None.
    """
    if not nums or x <= 0:
        return None

    def sieve(n):
        """Helper function to generate prime numbers up to n."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i, is_prime in enumerate(primes) if is_prime]
    max_num = max(nums)
    prime_numbers = sieve(max_num)
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if i in prime_numbers else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

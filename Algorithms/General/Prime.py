import math
import random
from typing import List


class Prime():
    def __init__(self, n: int = 100):
        self.rand = self.find_prime(n)
        self._prev: List[int] = []

    # Setters and Getters
    @property
    def rand(self):
        return self._rand

    @rand.setter
    def rand(self, v):
        self._rand = v

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, n):
        if n:
            self._prev.append(n)
        else:
            self._prev = []

    # Prime Methods
    def find_prime(self, n: int = 100) -> int:
        """
        Recusrive function that find a prime number from 2 to n

        Input:
        ------
        n -> Maximum number. Define a range between 2 and n.

        Return:
        ------
        A prime number in the range 2 and n.
        """

        # Odd numbers
        rand_num = random.randrange(1, n, 2)

        # 1 is not prime, then increase to 2
        if rand_num == 1:
            rand_num += 1

        if not self.is_prime(rand_num):
            return self.find_prime(n)
        return rand_num

    def new_rand(self, n: int = 10, counter: int = 0):
        """
        Get a new random prime number from find_prime method
        and check wether the number was generated before.
        If wasn't, it updates both attributes.

        Input:
        ------
        n       -> Maximum number. Define a range between 2 and n.
        counter -> count iteration of recursive function in order
                   to terminate after 500 iterations.

        Return:
        ------
        A prime number in the range 2 and n.
        """

        random_num = self.find_prime(n)

        # Abort recursion after 500 iterations
        if counter == 500:
            raise ValueError("Couldn't find a new prime number in that range!")

        if random_num in self.prev or random_num == self.rand:
            print(random_num)
            counter += 1
            return self.new_rand(n, counter)

        return random_num

    def new_prime(self, n: int = 10):
        """
        Update the current prime number to a new one.

        Input:
        ------
        n -> Maximum number. Define a range between 2 and n.

        Output:
        ------
        Print an error message if a new prime number was not found.
        """

        try:

            # Find new prime
            new_num = self.new_rand(n)

        # Too many iterations
        except ValueError as err:

            # Couldn't find a new prime
            print(err)

        # Update attributes
        else:
            self.prev = self.rand
            self.rand = new_num
            return self.rand

    def is_prime(self, n: int) -> bool:

        # Less than or equal to 1 -> not a prime
        if n <= 1:
            return False

        # 2 is a prime number
        if n == 2:
            return True

        # Any number greater than 2, divided by 2
        # Without a remainder is not a prime number
        if n % 2 == 0:
            return False

        # Iteration over odd numbers up to
        # the square root of n.
        for x in range(3, int(math.sqrt(n)) + 1, 2):

            # Ensure division outputs an integer
            if n % x == 0:

                # If so, not a prime number!
                return False

        # All tests passed --> Prime number!
        return True

    def __str__(self):
        """
        Returns a string with Current Prime,
        and Previous Primes whereas previous primes
        are listed in the order they were generated
        (from most recent to least recent)
        """
        string = f'Current Prime: {self.rand}'
        string += f'\nPrevious Primes: {[i for i in self.prev[-1 : : -1]]}'
        return string


def test():
    test = Prime()
    test.new_prime(100)
    test.new_prime(100)

    # Prime numbers from 1 to 1000
    prime_ls = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
                109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
                173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
                293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
                367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
                433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
                499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
                577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
                643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709,
                719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
                797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
                863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
                947, 953, 967, 971, 977, 983, 991, 997]

    new_ls = []
    for i in range(1, 1000):
        if test.is_prime(i):
            new_ls.append(i)

    assert new_ls == prime_ls

    # Find a randon prime number without
    # modifying the instance's attributes (rand, prev)
    print(test.new_rand(n=10000))
    print(test.rand, test.prev)
    print(test)
    print(test.find_prime(n=10000))


if __name__ == "__main__":
    test()

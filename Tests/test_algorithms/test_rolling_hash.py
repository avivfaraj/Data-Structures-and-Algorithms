from Algorithms.General.Rolling_Hash import rol_hash
from Algorithms.General.Prime import Prime
import pytest


@pytest.mark.parametrize("sample_str, n",
                         [("This is just a test to check that rolling hash matches regular hash", 4),
                          ("Second test with different window size", 10)])
def test_rolling_hash(sample_str: str, n: int) -> None:
    # Create a new instance
    prime_inst = Prime()

    # Store prime number
    prime_num = prime_inst.rand

    sample_str = "This is just a test to check that rolling hash matches regular hash"

    # Window size
    n = 4

    # Loop over windows with size 'n'
    for i in range(len(sample_str) - n):

        # Substring - window
        sub_str = sample_str[i: i + n]

        # Regular formula to calculate hash
        # Less efficient because of the number of operations
        # required such as multiplication / division ....
        reg_hash = sum(ord(sub_str[j]) * 256 ** (n - j - 1) for j in range(n)) % prime_num

        hash_ = -1

        # First iteration - no previous hash
        if i == 0:
            hash_ = rol_hash(sub_str, prime_num)

        # Other iterations - subtract first char contribution
        # and add the new char's contribution to the overall hash
        else:
            hash_ = rol_hash(sub_str, prime_num, sample_str[i - 1], hash_)

        # Ensure both hashes are the same!
        assert hash_ == reg_hash, "Something is wrong"

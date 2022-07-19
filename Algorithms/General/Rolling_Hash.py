from Algorithms.General.Prime import Prime


def rol_hash(text: str,
             prime: int,
             subtract: str = "",
             last_hash: int = -1) -> int:
    """
    Calculate hash of a text using a prime number.
    If substract and last_hash were entered, it calculates
    hash using rolling hash algorithm.

    Input:
    ------
    text -> Text to be converted into hash (str)
    prime -> A prime number (int)
    substract -> Character to be subtracted from the last hash (str).
    last_hash -> Last hash value (int).

    Return:
    ------
    The new hash value (int).

    """
    # Initialize vars
    n = len(text)
    hash_ = 0

    # Ensure new rolling hash
    if last_hash == -1:

        # Iterate each character in text
        for i, char in enumerate(text):
            # Convert character to number
            # (ASCII * 256 ^(n-i-1)) % prime_number
            # The power of 256 - zero for the right-most character
            hash_ += ord(char) * 256 ** (n - i - 1)
            hash_ %= prime

    # Rolling hash
    else:
        # Calculate Hash according to the last Hash:
        # Subtracting the hash value of the left-most character
        # of the previous text, and adding the hash value of
        # the right-most character in the new text.
        sub = last_hash - ord(subtract) * 256 ** (n - 1) % prime
        hash_ = ((sub * 256) % prime + ord(text[-1])) % prime

    return hash_


def test():
    # Create a new instance
    prime_inst = Prime()

    # Store prime number
    prime_num = prime_inst.rand
    print("Current Prime Number:", prime_num)

    # Hashing "This" (base 256)
    # T -- 84
    # h -- 104
    # i -- 105
    # s -- 115
    hash_ = rol_hash("This", prime_num)
    assert hash_ == (84 * 256 ** 3 +
                     104 * 256 ** 2 +
                     105 * 256 + 115) % prime_num, "Something is wrong"

    # Checking the rolling hash --> From "This" to "his "
    # h -- 104
    # i -- 105
    # s -- 115
    # whitespace - 32
    hash_ = rol_hash("his ", prime_num, subtract="T", last_hash=hash_)
    assert hash_ == (104 * 256 ** 3 +
                     105 * 256 ** 2 +
                     115 * 256 + 32) % prime_num

    print("Rolling Hash works fine!")


if __name__ == "__main__":
    test()

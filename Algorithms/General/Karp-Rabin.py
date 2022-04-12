from Rolling_Hash import rol_hash
from Prime import Prime




def karp_rabin_randomized(text: str, pattern: str, output: bool = False) -> int:
    """
    Karp-Rabin is a string matching algorithm that utilizes hash values
    using a random prime number for faster implementation.
    If a False match occurs, the prime number is changed to another
    random prime number, and rolling hash starts again. 

    Input:
    ------
    text -> Full text (str)
    pattern -> String to be found in the full text (str)
    output -> True to print iterations - substrings and hash values (bool).

    Output:
    ------
    If output is True, it prints every iteration 
    
    Return:
    ------
    The starting index of the first occurrence of pattern in text.
    If not found, returns -1.

    """
    # Variables
    match = False
    m, n = len(text), len(pattern)
    i, start_index = 0, -1
    new_prime = True

    # Prime instance
    p_inst = Prime(300)

    # Random Prime number
    prime = p_inst.rand

    # Hashing pattern using random prime number
    pattern_hash = rol_hash(pattern, prime)

    # Print pattern and its hash value
    if output:
        print("Pattern: " + pattern +", Hash: "+ str(pattern_hash))

    # Iterate over windows (substrings) with length similar to pattern 
    while not match and i < m - n:

        # Ensure first time using this prime number
        if new_prime:

            # Ensure not first iteration
            if i != 0:

                # Update Prime instance to a new prime number
                p_inst.new_prime(300)

                # Store prime number
                prime = p_inst.rand

                # Compute new hash value for pattern
                pattern_hash = rol_hash(pattern, prime)

                # Print pattern and its new hash value
                if output:
                    print("Pattern: " + pattern +", New Hash: "+ str(pattern_hash))

            # Hash window (substring of text) with the new prime number
            window_hash = rol_hash(text[i:i+n], prime)

            # Set to False --> to use rolling hash next iterations (Faster computation)
            new_prime = False

        # Same prime --> Rolling hash
        else:
            window_hash = rol_hash(text[i:i+n],prime, text[i-1],window_hash)

        # Print window and its hash value 
        if output:
            print("Widow: \'" + text[i:i+n] +"\', Hash: "+ str(window_hash))
        
        # Ensure hash values are the same
        if window_hash == pattern_hash:

            # Ensure the pattern and the window are the same string!
            # There is a chance that the hash value will be the same
            # But the string themselves are different. Hence, it is
            # required to check if the string do actually match. 
            if pattern == text[i:i+n]:

                # Stop iteration
                match = True

                # Store starting index
                start_index = i

            else:

                # Set to True --> to change prime number
                # It adds randomization since it prevents
                # the same exact error from occuring again.
                new_prime = True
                
        i += 1

    return start_index



def test():
    text = "This is just an example"
    pattern = "jua"
    print(karp_rabin_randomized(text, pattern, True))

if __name__ == "__main__":
    test()
    help(karp_rabin_randomized)


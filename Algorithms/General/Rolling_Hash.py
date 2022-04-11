from Prime import Prime

def rol_hash(text: str, 
			 prime: int, 
			 subtract: str = "", 
			 last_hash: int = -1) -> int:

    n = len(text)
    hash_ = 0
    if last_hash == -1:
        for i,char in enumerate(text):
            hash_ += ord(char) * 256 ** (n-i-1)
            hash_ %= prime
    else:
        hash_ = (((last_hash - ord(subtract)* 256 ** (n - 1)%prime) * 256)%prime + ord(text[-1]))%prime
        
    return hash_

def test():
	# Create a new instance
	prime_inst = Prime()

	# Store prime number
	prime_num = prime_inst.rand
	print("Current Prime Number: ", prime_num)

	# Hashing "This" (base 256)
	# T -- 84
	# h -- 104
	# i -- 105
	# s -- 115 
	hash_ = rol_hash("This", prime_num)
	assert hash_ == (84*256**3 + 104*256**2 + 105*256 + 115) % prime_num, "Something is wrong"

	# Checking the rolling hash --> From "This" to "his "
	# h -- 104
	# i -- 105
	# s -- 115
	# whitespace - 32
	hash_ = rol_hash("his ", prime_num, subtract = "T", last_hash = hash_)
	assert hash_ == (104*256**3 + 105*256**2 + 115*256 + 32) % prime_num

	print("Rolling Hash works fine!")

if __name__ == "__main__":
	test()

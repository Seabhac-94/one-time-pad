import random

# basic XOR function to underdtand the concept.
# def xor(x, s):
#     # insert code here
#     print(bin(x), 'xor', bin(s), '=', bin(x ^ s))
#
#
# xor(4, 8)
# xor(4, 4)
# xor(255, 1)
# xor(255, 128)


# implementing one time pad
def generate_key_stream(n):
    return bytes([random.randrange(0, 256) for i in range(n)])


def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes(key_stream[i] ^ message[i] for i in range(length))


# done by 'opposition'
message = "DO ATTACK"
message = message.encode()
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, message)

print(message)
print(key_stream)
print(cipher)

# attempting to 'break'
# shows that cipher can be decrypted to any message of the same length
print(cipher)
message = "NO ATTACK"
message = message.encode()
guess_key_stream = xor_bytes(message, cipher)
print(xor_bytes(guess_key_stream, cipher))

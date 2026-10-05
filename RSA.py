def pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2) == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d


def generate_keys():
    p = 61  # Example prime number
    q = 53  # Example prime number
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 17  # Example public exponent
    d = mod_inverse(e, phi)
    return e, d, n


def encrypt(message, e, n):
    outmessage = ""
    for char in message:
        ascii_value = ord(char)
        encrypted_value = pow(ascii_value, e, n)
        outmessage += str(encrypted_value) + " "
    return outmessage.strip()


def decrypt(message, d, n):
    outmessage = ""
    for num_str in message.split():
        encrypted_value = int(num_str)
        decrypted_ascii = pow(encrypted_value, d, n)
        outmessage += chr(decrypted_ascii)
    return outmessage


def main():
    e, d, n = generate_keys()

    print(f"Public Key: (e={e}, n={n})")
    print(f"Private Key: (d={d}, n={n})")

    message = "HELLO"
    print(f"Original Message: {message}")

    encrypted_message = encrypt(message, e, n)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, d, n)
    print(f"Decrypted Message: {decrypted_message}")


if __name__ == "__main__":
    main()
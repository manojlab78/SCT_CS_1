def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():  # only letters
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            # shift logic
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char  # keep symbols same

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def brute_force(text):
    results = []

    for shift in range(26):
        decrypted = decrypt(text, shift)
        results.append(f"Shift {shift}: {decrypted}")

    return results
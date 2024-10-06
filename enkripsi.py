def encrypt(text, shift=5):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

plain_text = "rumah 56"
encrypted_text = encrypt(plain_text)
print(f"Plaintext: {plain_text}")
print(f"Encrypted text: {encrypted_text}")

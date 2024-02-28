def ceaser_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if c.isalpha():
            c_encoded = (ord(c) + shift)
            cipher_text += chr(c_encoded)
        else:
            cipher_text += c
    return cipher_text

import base64


def encode_base64(text):
    text_bytes = text.encode("utf-8")
    encoded_bytes = base64.b64encode(text_bytes)
    return encoded_bytes.decode("utf-8")


def decode_base64(text):
    encoded_bytes = text.encode("utf-8")
    decoded_bytes = base64.b64decode(encoded_bytes)
    return decoded_bytes.decode("utf-8")


def encode_binary(text):
    binary_text = []
    for letter in text:
        binary_text.append(format(ord(letter), "08b"))
    return " ".join(binary_text)


def decode_binary(text):
    binary_text = text.split(" ")
    decoded_text = []
    for binary_letter in binary_text:
        decoded_text.append(chr(int(binary_letter, 2)))
    return "".join(decoded_text)

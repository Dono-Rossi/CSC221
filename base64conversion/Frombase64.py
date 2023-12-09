base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def text_to_base64(text):
    text_bytes = text.encode('utf-8')

    base64_output = ""
    index = 0
    while index < len(text_bytes):
        chunk = text_bytes[index:index + 3]

        padding = 3 - len(chunk)
        if padding:
            chunk += bytes([0] * padding)

        value = (chunk[0] << 16) + (chunk[1] << 8) + chunk[2]

        for i in range(4):
            base64_output += base64_chars[(value >> (18 - 6 * i)) & 63]

        if padding:
            base64_output = base64_output[:-padding] + '=' * padding

        index += 3

    if base64_output.endswith('='):
        base64_output = base64_output[:-1]

    return base64_output

with open('justbits.txt', 'r') as file:
    text_to_convert = file.read()

base64_text = text_to_base64(text_to_convert)

print(base64_text)


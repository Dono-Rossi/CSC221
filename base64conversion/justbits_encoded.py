def base64_to_text(base64_input):
  base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

  def get_value(char):
      return base64_chars.index(char) if char in base64_chars else None

  while base64_input.endswith('='):
      base64_input = base64_input[:-1]

  index = 0
  decoded_text = ""
  while index < len(base64_input):
      chunk = base64_input[index:index + 4]

      if all(char in base64_chars for char in chunk):
          value = 0
          for i in range(4):
              value <<= 6
              if i < len(chunk):
                  value += get_value(chunk[i])

          decoded_text += chr((value >> 16) & 255)
          if len(chunk) >= 3 and chunk[2] != '=':
              decoded_text += chr((value >> 8) & 255)
          if len(chunk) == 4 and chunk[3] != '=':
              decoded_text += chr(value & 255)

          index += 4
      else:
          break 

  return decoded_text

with open('justbits_encoded.txt', 'r') as file:
  base64_text = file.read().strip() 

decoded_text = base64_to_text(base64_text)

print(decoded_text)


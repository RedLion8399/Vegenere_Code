from Functions import decode, endcode, letter_value, value_letter

while True:
    try:
        code = input("Code:").lower()
        code_len = len(code)
        code_numbers = decode(code, code_len)
        key_input = True
        break
    except KeyError:
        print("Bitte geben sie nur Buchstaben des lateinischen Alphabets ein.") 

while True:
    try:
        key = input("Schlüssenwort:").lower()
        key_len = len(key)
        key_code = decode(key, key_len)
        code_input = True
        break
    except KeyError:
        print("Bitte geben sie nur Buchstaben des lateinischen Alphabets ein.") 

message = []
k_i = 0
for c_i in range(code_len):
    if code_numbers[c_i] == " ":
        message.append(" ")
    else:
        value = code_numbers[c_i] - key_code[k_i]
        if k_i + 1 < key_len:
            k_i += 1
        elif k_i + 1 == key_len:
            k_i = 0
        if value < 0:
            value += 26
        message.append(value)

print("".join(endcode(message, len(message))))
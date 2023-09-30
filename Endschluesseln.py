from Functions import decode, endcode, letter_value, value_letter

message = []
code = 0
key = 0
k_i = 0         # k_i ist der Key index

while code == 0:
    try:
        code = input("Code:").lower()
        code_len = len(code)
        code_numbers = decode(code, code_len)
        key_input = True
    except KeyError:
        code = 0
        print("Bitte geben sie nur Buchstaben des lateinischen Alphabets ein.") 

while key == 0:
    try:
        key = input("Schlüssenwort:").lower()
        key_len = len(key)
        key_code = decode(key, key_len)
        code_input = True
    except KeyError:
        key = 0
        print("Bitte geben sie nur Buchstaben des lateinischen Alphabets ein.") 

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
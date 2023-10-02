from Functions import decode, endcode, letter_value, value_letter

code = []
message = 0
key = 0
k_i = 0         # k_i ist der Key index

while message == 0:
    try:
        message = input("Nachricht:").lower()
        mes_len = len(message)
        mes_code = decode(message, mes_len)
        key_input = True
    except KeyError:
        message = 0
        print("Bitte geben sie nur Buchstaben des lateinischen Alphabets ein.") 

while key == 0:
    try:
        key = input("Schlüssenwort:").lower()
        key_len = len(key)
        key_code = decode(key, key_len)
        mes_input = True
    except KeyError:
        key = 0
        print("Bitte geben sie nur Buchstaben des lateinischen Alphabets ein.") 

for m_i in range(mes_len):
    if mes_code[m_i] == " ":
        code.append(" ")
    else:
        value = mes_code[m_i] + key_code[k_i]
        if k_i + 1 < key_len:
            k_i += 1
        elif k_i + 1 == key_len:
            k_i = 0
        if value > 25:
            value -= 26
        code.append(value)

print("".join(endcode(code, len(code))))
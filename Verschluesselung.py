from Functions import decode, endcode, letter_value, value_letter

while True:
    try:
        message = input("Nachricht:").lower()
        mes_len = len(message)
        mes_code = decode(message, mes_len)
        key_input = True
        break
    except KeyError:
        print("Bitte geben sie nur Buchstaben des lateinischen Alphabets ein.") 

while True:
    try:
        key = input("Schlüssenwort:").lower()
        key_len = len(key)
        key_code = decode(key, key_len)
        mes_input = True
        break
    except KeyError:
        print("Bitte geben sie nur Buchstaben des lateinischen Alphabets ein.") 

k_i = 0
code = []
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
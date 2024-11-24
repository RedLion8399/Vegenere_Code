from Functions import Text, decrypt

message: Text = Text()
key: Text = Text()
message.get_user_input("Nachricht: ")
key.get_user_input("Schlüsselwort: ")

k_i = 0
code = []

for m_i in range(message.len):
    if message.code[m_i] == " ":
        code.append(" ")
    else:
        value = message.code[m_i] + key.code[k_i]
        if k_i + 1 < key.len:
            k_i += 1
        elif k_i + 1 == key.len:
            k_i = 0
        if value > 25:
            value -= 26
        code.append(value)

print("".join(decrypt(code, len(code))))

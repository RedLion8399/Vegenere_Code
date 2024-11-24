from Functions import Text, decrypt

message: Text = Text("Nachricht: ")
key: Text = Text("Schlüsselwort: ")

k_i = 0
code: list[int | str] = []

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

print(decrypt(code, len(code)))

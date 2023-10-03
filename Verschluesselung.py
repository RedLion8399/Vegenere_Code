from Functions import Text, endcode

message = Text()
Key = Text()
message.user_input("Nachricht: ")
Key.user_input("Schlüsselwort: ")

k_i = 0
code = []

for m_i in range(message.len):
    if message.code[m_i] == " ":
        code.append(" ")
    else:
        value = message.code[m_i] + Key.code[k_i]
        if k_i + 1 < Key.len:
            k_i += 1
        elif k_i + 1 == Key.len:
            k_i = 0
        if value > 25:
            value -= 26
        code.append(value)

print("".join(endcode(code, len(code))))
from Functions import Text, decrypt

code: Text = Text()
key: Text = Text()
code.get_user_input("Code: ")
key.get_user_input("Schlüsselwort: ")

value: int
message: list[int | str] = []
k_i: int = 0

for c_i in range(code.len):
    if code.code[c_i] == " ":
        message.append(" ")
    else:
        value = code.code[c_i] - key.code[k_i]
        if k_i + 1 < key.len:
            k_i += 1
        elif k_i + 1 == key.len:
            k_i = 0
        if value < 0:
            value += 26
        message.append(value)

print("".join(decrypt(message, len(message))))

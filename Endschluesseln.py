from Functions import Text, endcode, letter_value, value_letter

code = Text()
Key = Text()
code.user_input("Code: ")
Key.user_input("Schlüsselwort: ")

message = []
k_i = 0
for c_i in range(code.len):
    if code.code[c_i] == " ":
        message.append(" ")
    else:
        value = code.code[c_i] - Key.code[k_i]
        if k_i + 1 < Key.len:
            k_i += 1
        elif k_i + 1 == Key.len:
            k_i = 0
        if value < 0:
            value += 26
        message.append(value)

print("".join(endcode(message, len(message))))
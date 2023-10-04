from Functions import Text, endcode, endcode_with_key

code = Text()
key = Text()
message = []
code.user_input("Code: ")
key.user_input("Schlüsselwort: ")

message = endcode_with_key(code.code, key.code)
print("".join(endcode(message, len(message))))
from Functions import Text

code: Text = Text("Code: ")
key: Text = Text("Schlüsselwort: ")

code.decrypt(key)

print(code.convert_to_letters())
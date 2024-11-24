from Functions import Text

message: Text = Text("Nachricht: ")
key: Text = Text("Schlüsselwort: ")

message.encrypt(key)

print(message.convert_to_letters())

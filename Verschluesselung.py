import Functions as Fc
from Functions import decode

letter_value = Fc.letter_value
message = 0
key = 0

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


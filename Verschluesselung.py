import Functions as Fc
from Functions import decode

letter_value = Fc.letter_value
key = input("Schlüssenwort:").lower()
message = input("Nachricht:").lower()

mes_len = len(message)
key_len = len(key)

mes_code = decode(message, mes_len)
key_code = decode(key, key_len)

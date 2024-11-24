class Text:
    def __init__(self) -> None:
        self.text = None
        self.len = None
        self.code = None
    
    def decode (self):
        code = []
        for i in range(self.len):
            value = self.text[i]
            code.append(letter_value[value])
        return code

    def user_input (self, user_message):
        while True:
            try:
                self.text = input(user_message).lower()
                self.len = len(self.text)
                self.code = self.decode()
                break
            except KeyError:
                print("Bitte geben sie nur Buchstaben des lateinischen Alphabets ein.") 
    

letter_value = {
    " " : " ",
    "a" : 0, 
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7,
    "i" : 8,
    "j" : 9,
    "k" : 10,
    "l" : 11,
    "m" : 12,
    "n" : 13,
    "o" : 14,
    "p" : 15,
    "q" : 16,
    "r" : 17,
    "s" : 18,
    "t" : 19,
    "u" : 20,
    "v" : 21,
    "w" : 22,
    "x" : 23,
    "y" : 24,
    "z" : 25
}

value_letter = {
    " " : " ",
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
    6 : "g",
    7 : "h",
    8 : "i",
    9  : "j",
    10 : "k",
    11 : "l",
    12 : "m",
    13 : "n",
    14 : "o",
    15 : "p",
    16 : "q",
    17 : "r",
    18 : "s",
    19 : "t",
    20 : "u",
    21 : "v",
    22 : "w",
    23 : "x",
    24 : "y",
    25 : "z"
} 

def endcode (text, text_len):
    code = []
    for i in range(text_len):
        value = text[i]
        code.append(value_letter[value])
    return code

class Text:
    def __init__(self) -> None:
        self.text: str
        self.len: int
        self.code: list[int | str]

    def encrypt (self) -> list[int | str]:
        for character in list(self.text):
            self.code.append(letter_value[character])
        return self.code

    def get_user_input (self, user_message: str) -> None:
        while True:
            try:
                self.text = input(user_message).lower()
                self.len = len(self.text)
                self.code = self.encrypt()
                break
            except KeyError:
                print("Bitte geben sie nur Buchstaben des lateinischen Alphabets ein.")


letter_value: dict[str, int | str] = {
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

value_letter: dict[int | str, str] = {
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

def decrypt (text, text_len: int) -> list[str]:
    code: list[str] = []
    for i in range(text_len):
        value = text[i]
        code.append(value_letter[value])
    return code

from __future__ import annotations

class Text:
    def __init__(self, message: str) -> None:
        self.text: str
        self.len: int
        self.code: list[int | str] = []
        self.new_text: str
        self.new_code: list[int | str] = []

        self.get_user_input(message)

    def get_user_input (self, user_message: str) -> None:
        while True:
            try:
                self.text = input(user_message).lower()
                self.len = len(self.text)
                self.code = self.convert_to_numbers()
                break
            except KeyError:
                print("Bitte geben sie nur Buchstaben des lateinischen Alphabets ein.")

    def convert_to_numbers (self) -> list[int | str]:
        for character in list(self.text):
            self.code.append(letter_value[character])
        return self.code

    def convert_to_letters (self) -> str:
        new_text: list[str] = []
        for number in self.new_code:
            new_text.append(value_letter[number])
        self.new_text = "".join(new_text)
        return self.new_text


    def decrypt (self, key: Text) -> str:
        while True:
            try:
                key.code.remove(" ")
            except ValueError:
                break

        for index, text_value in enumerate(self.code):
            if text_value == " ":
                self.new_code.append(" ")
                continue
            key_value = key.code[index % len(key.code)]
            new_value: int = text_value - key_value
            if new_value < 0:
                new_value += 26
            self.new_code.append(new_value)
        return self.convert_to_letters()

    def encrypt (self, key: Text) -> str:
        while True:
            try:
                key.code.remove(" ")
            except ValueError:
                break

        for index, text_value in enumerate(self.code):
            if text_value == " ":
                self.new_code.append(" ")
                continue
            key_value = key.code[index % len(key.code)]
            new_value: int = text_value + key_value
            if new_value > 25:
                new_value -= 26
            self.new_code.append(new_value)

        return self.convert_to_letters()

    def endcode_with_key(code, key):
        message = []
        code_len = len(code)
        key_len = len(key)
        k_i = 0
        for c_i in range(code_len):
            if code[c_i] == " ":
                message.append(" ")
            else:
                value = code[c_i] - key[k_i]
                if k_i + 1 < key_len:
                    k_i += 1
                elif k_i + 1 == key_len:
                    k_i = 0
                if value < 0:
                    value += 26
                message.append(value)
        return message


    def remove_whitespace(text):
        without_whitespace = []
        for letter in text:
            if letter != " ":
                without_whitespace.append(letter)
        return without_whitespace

    def counter(text):
        code = {}
        highest = [0, 0]
        for i in text:
            try:
                code[i] += 1
            except KeyError:
                code[i] = 1
                for letter, count in code.items():
                    if count > highest[1]:
                        highest[0] = letter
                        highest[1] = count
        
        Verschiebung = letter_value[highest[0]] - 4
        if Verschiebung < 0:
            Verschiebung += 26
        return Verschiebung

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

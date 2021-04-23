#Vegenere Cipher

#Создаем класс для определения используемого пароля дешифровки и используемого алфавита

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        #список для определения, на сколько букв нужно сделать сдвиг по алфавиту
        self.num_key = []
        for i in self.key:
            self.num_key.append(alphabet.find(i))
        print(self.num_key)

    # Определяем функцию, которая будет осуществлять сдвиг буквы по заданому алфавиту
    # на определенное количество символов - будет использована при кодировании/декодировании.
    # Алфавит *2, чтобы осуществить сдвиг, если алфавит кончится
    def shift(self, letter, shift_num):
        self.letter = letter
        self.shift_num = shift_num
        print((getattr(self, 'alphabet') * 2).find(self.letter), self.shift_num)

        result_num = (getattr(self, 'alphabet') * 2).find(self.letter) + self.shift_num
        return (getattr(self, 'alphabet') * 2)[result_num]

    def encode(self, text):
        self.text = text
    #если сообщение длиннее пароля, повторяем последовательность несколько раз
        num_key_multiplied = self.num_key * (len(self.text) // len(self.num_key) + 1)
        encoded_string = ''
        j = 0
        for i in self.text:
    #если символа в алфавите нет, оставляем как есть
            if getattr(self, 'alphabet').find(i) == -1:
                encoded_string += i
            else:
                encoded_string += self.shift(i, num_key_multiplied[j])
                j += 1
        return encoded_string

    def decode(self, text):
        self.text = text

        decoded_string = ''
        j = 0
        num_key_multiplied = self.num_key * (len(self.text) // len(self.num_key) + 1)
        for i in self.text:
            if getattr(self, 'alphabet').find(i) == -1:
                decoded_string += i
            else:
                decoded_string += self.shift(i, -num_key_multiplied[j])
                j += 1
        return decoded_string



# Examples
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key1 = 'password'
coding = VigenereCipher(key1, alphabet)
print(coding.encode('waffles'))
print(coding.decode('laxxhsj'))
key2 = 'lemon'
coding1 = VigenereCipher(key2, alphabet)
print(coding.encode('attackatdawn'))
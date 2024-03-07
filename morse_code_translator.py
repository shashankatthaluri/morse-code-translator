import colorama
from colorama import Fore, Style

class MorseCodeTranslator:
    def __init__(self):
        self.morse_code_dict = self.create_morse_code_dict()

    def create_morse_code_dict(self):
        morse_code_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.'
        }
        return morse_code_dict

    def english_to_morse(self, text):
        morse_code_list = [self.morse_code_dict[char] if char in self.morse_code_dict else char for char in text]
        return ' '.join(morse_code_list)

    def morse_to_english(self, morse_code):
        morse_code_dict_reverse = {value: key for key, value in self.morse_code_dict.items()}
        morse_code_list = morse_code.split(' ')
        english_text = ''.join([morse_code_dict_reverse[code] if code in morse_code_dict_reverse else code for code in morse_code_list])
        return english_text

def print_colored(text, color):
    return f"{color}{text}{Style.RESET_ALL}"

def main():
    colorama.init()  # Initialize colorama

    translator = MorseCodeTranslator()

    while True:
        print(print_colored("Morse Code Translator", Fore.MAGENTA))
        print("1. Translate English to Morse Code")
        print("2. Translate Morse Code to English")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            english_text = input(print_colored("Enter English text: ", Fore.CYAN)).upper()
            morse_code_text = translator.english_to_morse(english_text)
            print(print_colored(f"Morse Code: {morse_code_text}\n", Fore.GREEN))
        elif choice == '2':
            morse_code_text = input(print_colored("Enter Morse code: ", Fore.CYAN))
            english_text = translator.morse_to_english(morse_code_text)
            print(print_colored(f"English Text: {english_text}\n", Fore.GREEN))
        elif choice == '3':
            print(print_colored("Exiting the Morse Code Translator. Goodbye!", Fore.RED))
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

# Morse Code Converter
# Morse code is a code where each letter of the English alphabet, each digit
# and various punctuation characters are represented by a series of dots
# and dashes. Write a program that asks the user to enter a string,
# and then converts that string to Morse code.

def main():
    user_string = UserString()
    morse_code = MorseCode(user_string)
    Results(morse_code)

def UserString():
    string = input('Enter a string to convert to morse code: ')
    return string

def MorseCode(string):
    # Space, Comma, Period, Question
    p_code      = [' ', '--.--', '.-.-.-', '..--..']
    
    d_code      = [ '-----', '.----', '..---', '...--', '....-', # 0 - 4
                    '.....', '-....', '--...', '---..', '----.' ]# 5 - 9
    
    a_code      = [ '.-', '-...', '-.-.', '-..', '.',            # A - E
                    '..-.', '--.', '....', '..', '.---',         # F - J
                    '-.-', '.-..', '--', '-.', '---',            # K - O
                    '.--.', '--.-', '.-.', '...', '-',           # P - T
                    '..-', '...-', '.--', '-..-', '-.-',         # U - Y
                    '--..'                                      ]# Z
    a_place = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    morse_code = ''

    for ch in string:
        
        if ch.isspace():
            morse_code += p_code[0]
        elif ch == ',':
            morse_code += p_code[1]
        elif ch == '.':
            morse_code += p_code[2]
        elif ch == '?':
            morse_code += p_code[3]
            
        elif ch.isdigit():
            for d in range(len(d_code)):
                if ch == str(d):
                    morse_code += d_code[d]

        elif ch.isalpha():
            for a in range(len(a_code)):
                if ch.title() == a_place[a]:
                    morse_code += a_code[a]

    return morse_code

def Results(morse):
    print()
    print('============ Your sentence in Morse Code below ===============')
    print(morse)
    
main()

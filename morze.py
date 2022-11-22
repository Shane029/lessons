morze_alphabet = {
    'a' : '.-',
    'b' : '-...',
    'c' : '-.-.',
    'd' : '-..',
    'e' : '.',
    'f' : '..-.',
    'g' : '--.',
    'h' : '....',
    'i' : '..',
    'j' : '.---',
    'k' : '-.-',
    'l' : '.-..',
    'm' : '--',
    'n' : '-.',
    'o' : '---',
    'p' : '.--.',
    'q' : '--.-',
    'r' : '.-.',
    's' : '...',
    't' : '-',
    'u' : '..-',
    'v' : '...-',
    'w' : '.--',
    'x' : '-..-',
    'y' : '-.--',
    'z' : '--..',
     '0'  : '-----',
     '1'  : '.----',
     '2'  : '..---',
     '3'  : '...--',
     '4'  : '....-',
     '5'  : '.....',
     '6'  : '-....',
     '7'  : '--...',
     '8'  : '---..',
     '9'  : '----.'
}

morze = input("Enter here :    ").lower()
chars = '~!@#$%^&*()_+}{/?.>,<'
morze_converted = ''
for i in morze:
    if i in chars:
        continue
    elif i == ' ':
        morze_converted += i
    else:
        morze_converted = morze_converted + morze_alphabet[i]
print(morze_converted)
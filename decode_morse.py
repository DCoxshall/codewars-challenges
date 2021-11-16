def decodeMorse(morse_code):
    morse_code = morse_code.replace("   ", " X ")
    print(morse_code)
    morse = morse_code.split()
    print(morse)
    message = ""
    for i in morse:
        if i == "X": 
            message += ' '
        else:
            message += MORSE_CODE[i]
    return message.strip()

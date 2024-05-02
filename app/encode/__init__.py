def encode(message, shift):
    alphabet = ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    partialStart = ''
    partialEnd = ''
    shiftedAlphabet = ''
    encodedMessage = ''

    if shift == 0:
        shiftedAlphabet = alphabet
    elif shift > 0 and shift < 26:
        partialStart = alphabet[:shift]
        partialEnd = alphabet[shift:]
        shiftedAlphabet = partialEnd + partialStart
    elif shift < 0 and shift > -26:
        shift = shift * (-1)
        partialStart = alphabet[:shift]
        partialEnd = alphabet[shift:]
        shiftedAlphabet = partialEnd + partialStart
    else:
        return("shift_error")
    
    for letter in message:
        letter_index = alphabet.index(letter)
        encodedMessage = encodedMessage + shiftedAlphabet[letter_index]

    return(encodedMessage)
from morse.mapping import MORSE

# Reverse the MORSE dictionary: ".-" -> "A"
REVERSE_MORSE = {value: key for key, value in MORSE.items()}

def decode_word(morse_word):
    """
    Decodes a single Morse word into text.
    Letters are separated by a space.
    """
    letters = morse_word.split()
    decoded_letters = []

    for symbol in letters:
        if symbol in REVERSE_MORSE:
            decoded_letters.append(REVERSE_MORSE[symbol])

    return "".join(decoded_letters)

def decode(morse_text):
    """
    Decodes a Morse code sentence into text.
    Words are separated by |.
    """
    words = morse_text.split("|")
    decoded_words = []

    for word in words:
        decoded_words.append(decode_word(word))

    return " ".join(decoded_words)

if __name__ == "__main__":
    # Example usage for one word
    MORSE_WORD = ".... .."
    print(decode_word(MORSE_WORD))  # HI

    # Example usage for one sentence
    MORSE_SENTENCE = ".... ..|--. ..- -.-- ..."
    print(decode(MORSE_SENTENCE))   # HI GUYS


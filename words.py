def print_upper_words(words):
    """
    Print out each word on a separate line, but in all uppercase.
    """
    for word in words:
        print(word.upper())


print_upper_words(["hello", "world"])


def print_some_upper_words(words):
    """
    Prints words only starting with the letter 'e' (whether lowercase or uppercase) in uppercase.
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


print_some_upper_words(["Elvis", "egg", "Eugene", "Frank"])


def print_other_upper_words(words, start_with):
    """
    Print only words that start with the declared letter(s) in uppercase.
    """

    for word in words:
        for letter in start_with:
            if word.startswith(letter):
                print(word.upper())


print_other_upper_words(
    ["a", "bra", "ca", "da", "bra"], start_with=["a", "c"])

#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':',
    handling extra whitespace and sentence boundaries correctly.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentences = []
    sentence = ""
    for char in text:
        if char.isalnum():  # Check for alphanumeric characters
            sentence += char
        elif sentence:  # If a sentence has been formed and punctuation is encountered
            sentences.append(sentence.strip())
            sentence = ""  # Reset for the next sentence

        if char in ".?:":  # Add punctuation to the current sentence
            sentence += char

    if sentence:  # Append the last sentence if not empty
        sentences.append(sentence.strip())

    for sentence in sentences:
        print(sentence)
        print()  # Print newline after each sentence

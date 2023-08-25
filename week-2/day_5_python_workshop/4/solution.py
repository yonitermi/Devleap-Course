import re

def main(s):
    # Split the string based on whitespace, comma, semicolon, or period.
    words = re.split(r'([\s,.;])', s)

    # For each word, capitalize it based on the provided rules.
    capitalized_words = [word.capitalize() if word and word[0].isalpha() else word for word in words]

    # Join the words back together
    result = ''.join(capitalized_words)

    return result




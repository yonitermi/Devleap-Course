import re

def main(sentence):
    # Split the sentence into words using regex
    words = re.findall(r'\w+', sentence)
    
    # Initialize variables to keep track of the longest word and its length
    longest_word = ""
    max_length = 0
    
    # Iterate through each word and find the longest one
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    
    return longest_word






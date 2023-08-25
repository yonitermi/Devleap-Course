def main(word, parts):
    parts_list = parts.split(',')
    parts_set = set(parts_list)  # Convert to set for O(1) lookup
    
    for i in range(1, len(word)):
        # Split the word into two parts
        first_part = word[:i]
        second_part = word[i:]
        
        # Check if both parts are in the list
        if first_part in parts_set and second_part in parts_set:
            return [first_part, second_part]
    
    return []

# Testing the function
if __name__ == "__main__":
    word_input = input("Enter the word: ")
    parts_input = input("Enter the comma separated parts: ")
    print(main(word_input, parts_input))


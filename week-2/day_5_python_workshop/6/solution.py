def main(bigstr, smallstr):
    # Check if every character's frequency in smallstr is <= its frequency in bigstr
    for char in set(smallstr):
        if smallstr.count(char) > bigstr.count(char):
            return False
    return True



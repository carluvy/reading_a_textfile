# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as file:
        words = file.readlines()

    return words


def count_words():
    text = read_file_content("./story.txt")

    for sentence in text:
        word_list = sentence.split()
        word_dict = {word: len(word) for word in word_list}
        return word_dict


if __name__ == "__main__":
    wordly = count_words()
    print(wordly)

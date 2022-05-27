# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word):
    # [assignment] Add your code here
    word_list = word.split()
    first_word = word_list[0].lower()
    second_word = word_list[1].lower()

    return True if sorted(first_word) == sorted(second_word) else False


if __name__ == '__main__':
    words = input('Enter two words separated by a space: ')
    print(find_anagrams(words))

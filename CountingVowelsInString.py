def count_vowels():
    word = str(input("Enter a word:"))
    count = 0
    for letter in word:
        if letter == "a" or letter == "A" or letter == "e" or letter == "E" or letter == "i" or letter == "I" or letter == "o" or letter == "O" or letter == "u" or letter == "U":
            count += 1
    print(count)
    return count


count_vowels()
# Create a list of odd numbers from 1 to 10 using a list comprehension and the range function.
import string

odd_numbers = [number for number in range(0,11) if number % 2 > 0]
# Using a list comprehension, create a list of the squares of the first 10 even numbers.
even_number_list = []
# create a list of 10 even numbers
while len(even_number_list)<=10:
    number =0
    if number%2 == 0:
        even_number_list.append(number)

square_even_numbers = [number**2 for number in even_number_list  ]
# Using a list comprehension, create a list of the first 10 letters of the alphabet in upper case.

ten_first_letters = [letter for letter in list(string.ascii_uppercase)[:10]]
# print(ten_first_letters)
# Using a list comprehension, create a list of the first 10 letters of the alphabet in lower case, but with their ASCII values.

ten_first_letters = [ord(letter)for letter in list(string.ascii_uppercase)[:10]]

# Using a list comprehension and the enumerate function, create a list of the first 10 letters of the alphabet along with their corresponding index values.

ten_first_letters_alt = [t for t in enumerate(list(string.ascii_uppercase)) if t[0] < 10]
# print(ten_first_letters_alt)

# Using a list comprehension and the zip function, create a list of the first 10 letters of the alphabet along with their corresponding ASCII values.
# could you show me this?
# Using a list comprehension, create a list of the first 10 words in a sentence, but with the vowels removed.
sentence = "He found the end of the rainbow and was surprised at what he found there."


vowels = ["a","e", "i", "o", "u", "A","E", "I", "O", "U"]

first_ten_words_without_vowels = ["".join([letter for letter in word if letter not in vowels]) for word in [word for word in sentence.split()[:10] ]]



print(first_ten_words_without_vowels)
# Using a list comprehension, create a list of the first 10 words in a sentence, but with the consonants removed.
sentence = "He found the end of the rainbow and was surprised at what he found there."


vowels = ["a","e", "i", "o", "u", "A","E", "I", "O", "U"]

first_ten_words_with_vowels = ["".join([letter for letter in word if letter  in vowels]) for word in [word for word in sentence.split()[:10] ]]

print(first_ten_words_with_vowels)
# Using a list comprehension and the filter function, create a list of the first 10 words in a sentence that are at least 4 characters long.
#
# Using a list comprehension and the map function, create a list of the first 10 words in a sentence, but with the first letter of each word capitalized.
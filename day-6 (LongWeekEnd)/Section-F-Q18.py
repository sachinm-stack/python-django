# Q18.Reusability — Function Library
# Build a small function library. Each function should be reusable. Then use them together in a final program.



# Write all 5 functions:
# 1. celsius_to_fahrenheit(c) → returns (c * 9/5) + 32
def celsius_to_fahrenheit(c):
    return (c* 9/5)+32
print(celsius_to_fahrenheit(0))


# 2. count_vowels(text) → returns count of a,e,i,o,u in text
def count_vowels(text):
    text = text.lower()
    return (text.count('a') +
            text.count('e') +
            text.count('i') +
            text.count('o') +
            text.count('u'))
print(count_vowels("education"))

# 3. reverse_string(text) → returns text reversed

def reverse_string(text):
    return text[::-1]

print(reverse_string("hello"))   # olleh



# 4. is_palindrome(text) → returns True if text == text reversed

def is_palindrome(text):
   return  text==text[::-1]
print(is_palindrome("racecar"))

# 5. word_count(sentence) → returns number of words

def word_count(sentence):
    return len(sentence.split())
print(word_count("I love Python programming"))

# Then call them to produce this output:
# celsius_to_fahrenheit(0) → 32.0
# celsius_to_fahrenheit(100) → 212.0
# count_vowels("Hello World") → 3
# reverse_string("python") → nohtyp
# is_palindrome("racecar") → True
# is_palindrome("hello") → False
# word_count("I love Python programming") → 4

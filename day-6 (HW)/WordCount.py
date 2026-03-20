# def count_words(text):
#     words=str(input("enter the sentence:"))
#     words




def count_words(text):
    words = text.split()     # splits sentence into list of words
    counts = {}              # empty dictionary
    for word in words:
         if word in counts:
            counts[word] += 1
         else:
            counts[word] = 1
    
    return counts

result = count_words("the cat sat on the mat the cat")
print(result)
# Expected: {"the":3, "cat":2, "sat":1, "on":1, "mat":1}

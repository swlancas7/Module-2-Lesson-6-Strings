# 1. Product Review Analysis

# Task 1: Keyword Highlighter

def capitalize_words(text, words_to_capitalize):
    words = text.split()
    for i, word in enumerate(words):
        if word in words_to_capitalize:
            words[i] = word.capitalize()
    return ' '.join(words)

text = "This product is really good. I'm impressed with its quality.",
"The performance of this product is excellent. Highly recommended!",
"I had a bad experience with this product. It didn't meet my expectations.",
"Poor quality product. Wouldn't recommend it to anyone.",
"The product was average. Nothing extraordinary about it."
words_to_capitalize = ["good", "excllent", "bad", "poor", "average"]

result = capitalize_words(text, words_to_capitalize)
print(result)



# Task 2: Sentiment Tally

from collections import Counter

items = [
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]]

tally = Counter(items)

print(tally)

# Task 3: Review Summary

def smart_truncate(content, length=30, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix
    

# 2. User Input Data Processor

#Task 1: Input Length Validator

name = input("Your first and last name: "). split(" ") if len(name) == 2: print("Name: ", name[0]. upper(), ", ", name[1].) 
else:
    print: "Invalid name length."
import re

# Open text File
with open("sample.txt","r") as text_file:
    text_data = text_file.read()
    # Remove new lines and extra spaces
    text_data = text_data.replace("\n", " ").strip()

# Split text into sentences
text_sentences = [sentenc for sentenc in text_data.split(".") if sentenc.strip()]

# Remove punctuation from text
text_without_signs = re.sub(r'[^\w\s]', '', text_data)
# Remove extra spaces
text_without_signs = " ".join(text_without_signs.split())

# Split text into words and convert to lower case
text_words = text_without_signs.split()
text_words = [word.lower() for word in text_words]

# Remove spaces and new lines from text to count letters
text_letters = text_without_signs.replace(" ","").replace("\n","")
text_letters = ''.join([char for char in text_letters if char.isalpha()])


# Count sentences, words, letters , average word length and most used word
sentence_count = len(text_sentences)
word_count = len(text_words)
letter_count = len(text_letters)
average_word_count = letter_count / word_count
most_used_word = max(text_words, key=text_words.count)
most_used_word_count = text_words.count(most_used_word)

print("Sentence count: " + str(sentence_count))
print("Word count: " + str(word_count))
print("Letter count: " + str(letter_count))
print("Average word count: " + str(average_word_count))
print("Most used word: " + str(most_used_word), "with " , most_used_word_count , " occurrences")


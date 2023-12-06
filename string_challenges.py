# Вывести последнюю букву в слове
word = 'Архангельск'
last_character = word[-1]
print(f"последняя буква: {last_character}")

# Вывести количество букв "а" в слове
word = 'Архангельск'
count_a = word.lower().count('а')
print(f"количество букв 'a' в слове {count_a}")


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowel = "ауоыиэяюёе"
vowel_cout = 0
for letter in word.lower():
    if letter in vowel:
        vowel_cout += 1
print(f"количество гласных букв в слове: {vowel_cout}")

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words_list = sentence.split()
print(f"количество слов в предложении: {words_list}")

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words_list = sentence.split()
for word in words_list:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words_count = len(sentence.split())
letters_count = len(sentence.replace(' ', ''))
avg_word_len = 0
if words_count > 0:
    avg_word_len = letters_count/words_count
print(f"усреднённая длина слова в предложении {avg_word_len}")
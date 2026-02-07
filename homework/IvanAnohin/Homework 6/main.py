text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)

words = text.split()
final_words = []

for word in words:
    if word[-1] in ',.':
        unsigned_word = word[:-1]
        punctuation = word[-1]
        new_word = unsigned_word + 'ing' + punctuation
        final_words.append(new_word)
    else:
        new_word = word + 'ing'
        final_words.append(new_word)

result_text = ' '.join(final_words)
print(result_text)

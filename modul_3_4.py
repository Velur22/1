def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        other_words_u = i.upper()
        root_word_u = root_word.upper()
        if root_word_u in other_words_u or other_words_u in root_word_u:
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)

def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
    return same_words


result1 = single_root_words('Лес', 'Лесополоса', 'Лесник', 'Село', 'Подлесок')
result2 = single_root_words('Лесополоса', 'Лес', 'Полоса', 'Лесник', 'Сопло')

print(result1)
print(result2)

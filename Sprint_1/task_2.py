def string_handler(string):
    word_list = []
    marks_list = []
    signs = [',', '!', '.', '?']
    # Второе абсолютно рабочее решение. В предыдущем проверка на длину !=0 использовалась для того,
    # чтобы исключить попадание в итоговый список слов пустых значений '' после отсечения символа.
    # Третий раз писать рабочее решение, но *другое*, я не буду :)
    for word in string.split():

        if word[-1] in signs:
            if word[-1] not in marks_list:
                marks_list.append(word[-1])

            word_without_sign = word[:-1]

            if word_without_sign not in word_list:
                word_list.append(word_without_sign)

        elif word not in word_list:
            word_list.append(word)

    print(word_list)
    print(marks_list)

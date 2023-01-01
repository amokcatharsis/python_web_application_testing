# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    def test_init_init_book_rating_is_empty_true(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # проверяем изначальное состояние словаря рейтинга
        assert len(new_books_collector.books_rating) == 0, 'Словарь рейтинга непустой'

    def test_init_init_favorites_is_empty_true(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # проверяем изначальное состояние списка Избранное
        assert len(new_books_collector.favorites) == 0, 'Список Избранное непустой'

    def test_add_new_book_add_two_different_books(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # добавляем две книги
        new_books_collector.add_new_book('Гордость и предубеждение и зомби')
        new_books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(new_books_collector.get_books_rating()) == 2, 'Количество книг !=2'

    def test_add_new_book_add_two_equal_books(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # добавляем две одинаковые книги
        new_books_collector.add_new_book('Гордость и предубеждение и зомби')
        new_books_collector.add_new_book('Гордость и предубеждение и зомби')
        # проверяем, что добавилась только одна книга
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 1
        assert len(new_books_collector.get_books_rating()) == 1, 'Количество одинаковых книг !=1'

    def test_add_new_book_base_rating_is_one_true(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # добавляем одну книгу в словарь books_rating
        new_books_collector.add_new_book('Гордость и предубеждение и зомби')
        # проверяем, что присваивается рейтинг 1 при передаче только имени книги
        assert new_books_collector.books_rating['Гордость и предубеждение и зомби'] == 1, 'Изначальный рейтинг != 1'

    def test_set_book_rating_set_rating_in_range_1_11(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # добавляем одну книгу в словарь books_rating
        new_books_collector.add_new_book('Гордость и предубеждение и зомби')
        # задаём рейтинг для добавленной книги
        new_books_collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        # проверяем, что рейтинг соответствует заданному
        assert new_books_collector.books_rating['Гордость и предубеждение и зомби'] == 5, 'Рейтинг не соответствует/' \
                                                                                          ' заданному'

    def test_set_book_rating_set_zero_rating(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # добавляем одну книгу в словарь books_rating
        new_books_collector.add_new_book('Гордость и предубеждение и зомби')
        # задаём рейтинг ниже минимального для добавленной книги
        new_books_collector.set_book_rating('Гордость и предубеждение и зомби', -2)
        # проверяем, что рейтинг ниже минимального не присвоился
        assert new_books_collector.get_books_rating() != -2, 'Задан рейтинг ниже минимального'

    def test_set_book_rating_set_rating_out_of_max_range(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # добавляем одну книгу в словарь books_rating
        new_books_collector.add_new_book('Гордость и предубеждение и зомби')
        # задаём рейтинг выше максимольного для добавленной книги
        new_books_collector.set_book_rating('Гордость и предубеждение и зомби', 15)
        # проверяем, что рейтинг выше максимального не присвоился
        assert new_books_collector.get_books_rating() != 15, 'Задан рейтинг выше максимального'

    def test_get_book_rating_return_book_rating_with_boundary_values(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # добавляем три уникальных книги в словарь books_rating
        new_books_collector.add_new_book('Страх')
        new_books_collector.add_new_book('И ненависть')
        new_books_collector.add_new_book('В Лас - Вегасе')
        # задаём рейтинг для добавленных книг
        new_books_collector.set_book_rating('Страх', 1)
        new_books_collector.set_book_rating('И ненависть', 5)
        new_books_collector.set_book_rating('В Лас - Вегасе', 10)
        # проверяем рейтинг == граничным значениям для заданных книг
        assert new_books_collector.get_book_rating('Страх') == 1, 'Рейтинг не соответствует заданному'
        assert new_books_collector.get_book_rating('И ненависть') == 5, 'Рейтинг не соответствует заданному'
        assert new_books_collector.get_book_rating('В Лас - Вегасе') == 10, 'Рейтинг не соответствует заданному'

    def test_get_books_with_specific_rating(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # добавляем пять уникальных книг
        new_books_collector.add_new_book('Страх')
        new_books_collector.add_new_book('И ненависть')
        new_books_collector.add_new_book('В Лас - Вегасе')
        new_books_collector.add_new_book('Ретеcт')
        new_books_collector.add_new_book('Сколько можно')
        # задаём рейтинг для добавленных книг
        new_books_collector.set_book_rating('Страх', 2)
        new_books_collector.set_book_rating('И ненависть', 2)
        new_books_collector.set_book_rating('Ретеcт', 5)
        new_books_collector.set_book_rating('В Лас - Вегасе', 5)
        new_books_collector.set_book_rating('Сколько можно', 5)
        # запоминаем списки
        books_with_rating_two = new_books_collector.get_books_with_specific_rating(2)
        books_with_rating_three = new_books_collector.get_books_with_specific_rating(5)
        # проверяем рейтинг для указанных книг
        assert len(new_books_collector.get_books_with_specific_rating(2)) == 2
        assert ['Страх', 'И ненависть'] == books_with_rating_two, 'Не все книги с заданным рейтингом 2 в списке'
        assert len(new_books_collector.get_books_with_specific_rating(5)) == 3
        assert ['В Лас - Вегасе', 'Ретеcт', 'Сколько можно'] == books_with_rating_three, 'Не все книги с заданным ' \
                                                                                         'рейтингом 3 в списке'

    def test_get_books_rating_return_dict_with_book_with_preset_rating(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # добавляем  книгу в словарь books_rating
        new_books_collector.add_new_book('Гордость и предубеждение и зомби')
        # задаём рейтинг для добавленных книг
        new_books_collector.set_book_rating('Гордость и предубеждение и зомби', 2)
        # проверяем значение рейтинга и тип возвращаемого объекта
        assert type(new_books_collector.books_rating) == dict, 'Метод возвращает не словарь'
        assert new_books_collector.books_rating['Гордость и предубеждение и зомби'] == 2, 'Рейтинг не соответствует' \
                                                                                          ' заданному'

    def test_add_book_in_favorites_add_one_book_in_favorites(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # добавляем  книгу в словарь books_rating
        new_books_collector.add_new_book('Гордость и предубеждение и зомби')
        # добавляем книгу в список Избранное
        new_books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        # проверяем, что книга в Избранном и длина списка Избранное = 1
        assert 'Гордость и предубеждение и зомби' in \
               new_books_collector.get_list_of_favorites_books(), 'Книга не добавлена в Избранное'
        assert len(new_books_collector.favorites) == 1, 'Длина списка не совпадает с количеством добавленных книг'

    def test_add_book_in_favorites_book_not_in_books_rating_cant_be_added_true(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # добавляем книгу, отсутствующую в словаре books_rating, в избранное
        new_books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        # проверяем, что книга не в Избранном и длина списка Избранное = 0
        assert 'Гордость и предубеждение и зомби' not in \
               new_books_collector.get_list_of_favorites_books(), 'Книга добавлена в Избранное'
        assert len(new_books_collector.favorites) == 0, 'Длина списка Избранное не 0'

    def test_delete_book_from_favorites_delete_one_book(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # добавляем  книгу в словарь books_rating
        new_books_collector.add_new_book('Гордость и предубеждение и зомби')
        # добавляем книгу в избранное
        new_books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        # проверяем, что книга в Избранном и длина списка Избранное = 1
        assert 'Гордость и предубеждение и зомби' in \
               new_books_collector.get_list_of_favorites_books(), 'Книга не добавлена в Избранное'
        assert len(new_books_collector.favorites) == 1, 'Длина списка не совпадает с количеством добавленных книг'
        # удаляем книгу из Избранного
        new_books_collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        # проверяем, что книга не в Избранном и длина списка Избранное = 0
        assert 'Гордость и предубеждение и зомби' not in \
               new_books_collector.get_list_of_favorites_books(), 'Книга не удалилась из Избранного'
        assert len(new_books_collector.favorites) == 0, 'Длина списка Избранное не 0'

    def test_get_list_of_favorites_books_return_list_with_one_book(self, new_books_collector):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры
        # добавляем  книгу в словарь books_rating
        new_books_collector.add_new_book('Гордость и предубеждение и зомби')
        # добавляем книгу в избранное
        new_books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        # проверяем, что возвращается список, книга в Избранном и длина списка Избранное = 1
        assert type(new_books_collector.favorites) == list, 'Метод возвращает не список'
        assert 'Гордость и предубеждение и зомби' in \
               new_books_collector.get_list_of_favorites_books(), 'Книга не добавлена в Избранное'
        assert len(new_books_collector.favorites) == 1, 'Длина списка не совпадает с количеством добавленных книг'
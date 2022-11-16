import unittest
import itertools
import string
import pymysql
import pymysql.cursors

password = ''


class UnitTestsArtificialWords(unittest.TestCase):
    # ok
    def test_print_lowercase(self):
        print('test_print_lowercase')

        lowercase_letters = list(string.ascii_lowercase)

        print(lowercase_letters)

    # ok
    def test_print_uppercase(self):
        print('test_print_uppercase')

        uppercase_letters = list(string.ascii_uppercase)

        print(uppercase_letters)

    # ok
    def test_print_words_with_1c(self):
        print('test_print_words_with_1c')

        lowercase_letters = list(string.ascii_lowercase)
        uppercase_letters = list(string.ascii_uppercase)
        all_numbers = range(0, 10)

        for c1 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
            print(c1)

    # ok
    def test_print_words_with_2c(self):
        print('test_print_words_with_2c')

        lowercase_letters = list(string.ascii_lowercase)
        uppercase_letters = list(string.ascii_uppercase)
        all_numbers = range(0, 10)

        for c1 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
            for c2 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                word = str(c1) + str(c2)
                print(word)

    # ok
    def test_print_words_with_3c(self):
        print('test_print_words_with_3c')

        lowercase_letters = list(string.ascii_lowercase)
        uppercase_letters = list(string.ascii_uppercase)
        all_numbers = range(0, 10)

        for c1 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
            for c2 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                for c3 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                    word = str(c1) + str(c2) + str(c3)
                    print(word)

    # ok
    def test_print_words_with_4c(self):
        print('test_print_words_with_4c')

        lowercase_letters = list(string.ascii_lowercase)
        uppercase_letters = list(string.ascii_uppercase)
        all_numbers = range(0, 10)

        for c1 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
            for c2 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                for c3 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                    for c4 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                        word = str(c1) + str(c2) + str(c3) + str(c4)
                        print(word)

    # ok
    def test_print_words_with_5c(self):
        print('test_print_words_with_5c')

        lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        uppercase_letters = list(string.ascii_uppercase)
        all_numbers = range(0, 10)

        for c1 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
            for c2 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                for c3 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                    for c4 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                        for c5 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                            word = str(c1) + str(c2) + str(c3) + str(c4) + str(c5)
                            print(word)


class UnitTestsArtificialWordsWithPrintableCharacters(unittest.TestCase):
    # ok
    def test_print_words_with_printable_ascii_characters(self):
        print('test_print_words_with_printable_ascii_characters')

        printable_ascii_characters = string.printable

        for c1 in printable_ascii_characters:
            print(c1)


class UnitTestsArtificialWordsIntoMySQL(unittest.TestCase):
    # ok
    def test_insert_words_with_one_character(self):
        print("test_insert_words_with_one_character")

        lowercase_letters = list(string.ascii_lowercase)
        uppercase_letters = list(string.ascii_uppercase)
        all_numbers = range(0, 10)

        for c1 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):

            x = {
                'word': str(c1)
            }

            try:
                connection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password=password,
                    db='artificial_words',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )

                with connection.cursor() as cursor:
                    try:
                        sql = "INSERT INTO `words` (`word`) VALUE (%s)"

                        cursor.execute(sql, (
                            x.get('word')
                        ))

                        connection.commit()

                        print('Word : ' + x.get('word') + ' : ok')

                        connection.close()
                    except Exception as e:
                        print("The record already exists (word " + x.get('word') + ") : " + str(e))

                        connection.close()
            except Exception as e:
                print("Problem connection MySQL : " + str(e))

    # ok
    def test_insert_words_with_2c(self):
        print("test_insert_words_with_2c")

        lowercase_letters = list(string.ascii_lowercase)
        uppercase_letters = list(string.ascii_uppercase)
        all_numbers = range(0, 10)

        for c1 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
            for c2 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                word = str(c1) + str(c2)

                x = {
                    'word': word
                }

                try:
                    connection = pymysql.connect(
                        host='localhost',
                        port=3306,
                        user='root',
                        password=password,
                        db='artificial_words',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor
                    )

                    with connection.cursor() as cursor:
                        try:
                            sql = "INSERT INTO `words` (`word`) VALUE (%s)"

                            cursor.execute(sql, (
                                x.get('word')
                            ))

                            connection.commit()

                            print('Word : ' + x.get('word') + ' : ok')

                            connection.close()
                        except Exception as e:
                            print("The record already exists (word " + x.get('word') + ") : " + str(e))

                            connection.close()
                except Exception as e:
                    print("Problem connection MySQL : " + str(e))

    # ok
    def test_insert_words_with_3c(self):
        print("test_insert_words_with_3c")

        lowercase_letters = list(string.ascii_lowercase)
        uppercase_letters = list(string.ascii_uppercase)
        all_numbers = range(0, 10)

        for c1 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
            for c2 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                for c3 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                    word = str(c1) + str(c2) + str(c3)

                    x = {
                        'word': word
                    }

                    try:
                        connection = pymysql.connect(
                            host='localhost',
                            port=3306,
                            user='root',
                            password=password,
                            db='artificial_words',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor
                        )

                        with connection.cursor() as cursor:
                            try:
                                sql = "INSERT INTO `words` (`word`) VALUE (%s)"

                                cursor.execute(sql, (
                                    x.get('word')
                                ))

                                connection.commit()

                                print('Word : ' + x.get('word') + ' : ok')

                                connection.close()
                            except Exception as e:
                                print("The record already exists (word " + x.get('word') + ") : " + str(e))

                                connection.close()
                    except Exception as e:
                        print("Problem connection MySQL : " + str(e))

    # ok
    def test_insert_words_with_4c(self):
        print("test_insert_words_with_4c")

        lowercase_letters = list(string.ascii_lowercase)
        uppercase_letters = list(string.ascii_uppercase)
        all_numbers = range(0, 10)

        for c1 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
            for c2 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                for c3 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                    for c4 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                        word = str(c1) + str(c2) + str(c3) + str(c4)

                        x = {
                            'word': word
                        }

                        try:
                            connection = pymysql.connect(
                                host='localhost',
                                port=3306,
                                user='root',
                                password=password,
                                db='artificial_words',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor
                            )

                            with connection.cursor() as cursor:
                                try:
                                    sql = "INSERT INTO `words` (`word`) VALUE (%s)"

                                    cursor.execute(sql, (
                                        x.get('word')
                                    ))

                                    connection.commit()

                                    print('Word : ' + x.get('word') + ' : ok')

                                    connection.close()
                                except Exception as e:
                                    print("The record already exists (word " + x.get('word') + ") : " + str(e))

                                    connection.close()
                        except Exception as e:
                            print("Problem connection MySQL : " + str(e))

    # ok
    def test_insert_words_with_5c(self):
        print("test_insert_words_with_5c")

        lowercase_letters = list(string.ascii_lowercase)
        uppercase_letters = list(string.ascii_uppercase)
        all_numbers = range(0, 10)

        for c1 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
            for c2 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                for c3 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                    for c4 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                        for c5 in itertools.chain(lowercase_letters, uppercase_letters, all_numbers):
                            word = str(c1) + str(c2) + str(c3) + str(c4) + str(c5)

                            x = {
                                'word': word
                            }

                            try:
                                connection = pymysql.connect(
                                    host='localhost',
                                    port=3306,
                                    user='root',
                                    password=password,
                                    db='artificial_words',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor
                                )

                                with connection.cursor() as cursor:
                                    try:
                                        sql = "INSERT INTO `words` (`word`) VALUE (%s)"

                                        cursor.execute(sql, (
                                            x.get('word')
                                        ))

                                        connection.commit()

                                        print('Word : ' + x.get('word') + ' : ok')

                                        connection.close()
                                    except Exception as e:
                                        print("The record already exists (word " + x.get('word') + ") : " + str(e))

                                        connection.close()
                            except Exception as e:
                                print("Problem connection MySQL : " + str(e))


if __name__ == '__main__':
    unittest.main()

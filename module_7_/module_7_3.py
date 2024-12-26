#"Оператор "with"
class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):
        all_words = dict()

        for i in self.file_names:
            words = []
            with open(i, 'r', encoding='utf-8') as file:
                for line in file:
                    for word in line.split():
                        if word[-1] not in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            words.append(word)
                        else:
                            words.append(word[:-1:])

            all_words[i] = words

        return all_words

    def find(self, word):
        result = dict()

        for name, words in WordsFinder.get_all_words(self).items():
            result[name] = words.index(word.lower()) + 1

        return result

    def count(self, word):
        result = dict()

        for name, words in WordsFinder.get_all_words(self).items():
            result[name] = words.count(word.lower())

        return result


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
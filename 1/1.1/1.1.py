import sys


def word_frequency(filename):
    freq = {}
    with open(filename, encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                if word:
                    freq[word] = freq.get(word, 0) + 1
    return freq


def print_word_frequency(filename):
    freq = word_frequency(filename)
    # Сортировка по убыванию частоты, затем по алфавиту
    for word, count in sorted(freq.items(), key=lambda item: (-item[1], item[0])):
        print(f"{word}: {count}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: word_freq.py <имя файла>")
        sys.exit(1)
    print_word_frequency(sys.argv[1])

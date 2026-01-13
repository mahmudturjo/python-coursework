def count_word_frequencies(text):
    frequencies = {}
    words = text.lower().split()

    for word in words:
        word = word.strip(".,!?")
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


if __name__ == "__main__":
    sample_text = "Security and privacy are important. Security matters."
    result = count_word_frequencies(sample_text)

    for word, count in result.items():
        print(word, ":", count)

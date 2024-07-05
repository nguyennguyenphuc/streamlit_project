import streamlit as st


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


def levenshtein_distance(token1, token2):
    distances = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1
    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                distances[t1][t2] = min(a, b, c) + 1

    return distances[len(token1)][len(token2)]


def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')
    if word:
        vocabs = load_vocab(r'.\word_correction\vocab.txt')
        leven_distances = {vocab: levenshtein_distance(
            word, vocab) for vocab in vocabs}
        correct_word = min(leven_distances, key=leven_distances.get)
        st.write('Correct word:', correct_word)
        st.write('Vocabulary:', vocabs)
        st.write('Distances:', leven_distances)


if __name__ == "__main__":
    main()

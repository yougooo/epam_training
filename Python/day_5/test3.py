from itertools import groupby


def main(text, lines=1):
    total_lines = text.replace('\n', ' ')
    total_words_list = total_lines.split()

    group_words = [(word,list(group)) for word,group in
                   groupby(sorted(total_words_list, key=str.lower))]

    return sorted(group_words, key=lambda x: len(x[1]), reverse=True)[0][0]


if __name__ == "__main__":
    test_set = 'apple orange banana banana orange'
    test_set_1 = """
               q w e r t y i o p
               a s d f g h j k l
               z x c v b n m
               """
    test_set_2 = """
               vqcg vqcg vqcg vqcg vqcg vqcg vqcg
               vqcg vqcg
               vqcg aaaa
                 """
    test_set_3 = """
                 taia ikm ikm ikm taia taia taia
                 ikm ikm ikm
                 """
    print(main(test_set, 1))



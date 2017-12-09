import sys


morze_dict =     {'A': '.-',     'B': '-...',   'C': '-.-.',
                  'D': '-..',    'E': '.',      'F': '..-.',
                  'G': '--.',    'H': '....',   'I': '..',
                  'J': '.---',   'K': '-.-',    'L': '.-..',
                  'M': '--',     'N': '-.',     'O': '---',
                  'P': '.--.',   'Q': '--.-',   'R': '.-.',
                  'S': '...',    'T': '-',      'U': '..-',
                  'V': '...-',   'W': '.--',    'X': '-..-',
                  'Y': '-.--',   'Z': '--..'
                  }

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

loop = lambda item: list(map(lambda x: '^' if x == '.' else '^^^', item))
encode_signal = lambda morze_letters: '_'.join(loop(morze_letters))

signal_dict = {key:encode_signal(item) for key,item in morze_dict.items()}

encode_words = lambda word: '___'.join([signal_dict[letter] for letter in word])


def encode_morze(text):
    text = text.upper()
    text = text.strip()
    text = ''.join([letter for letter in text if letter in letters])
    return '_______'.join([encode_words(word) for word in text.split(' ')])
    #return '_______'.join(list(map(encode_words, text.split(' '))))


if __name__ == '__main__':

    s = sys.argv[1]
    print(encode_morze(s))
    print(encode_morze('Morze code'))
    print(encode_morze('Prometheus'))
    print(encode_morze('SOS'))
    print(encode_morze('1'))


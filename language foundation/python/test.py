import python_script_test

black_words = set()
for line in open('black_words', 'r', encoding='utf-8'):
    line = line.strip('\n')
    black_words.add(line)
print(black_words)




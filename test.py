import os

directory = r'/Users/student/Desktop/maildir'
start = False
sentences_l = []
single_s = []

for root, subdirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.'):
            docs = open(os.path.join(root, file), 'r')
            content = docs.readlines()

            for item in content:
                if '. ' in item:
                    item = item.strip().replace('\t', '').replace('?', '').replace('/',' ')
                    item = item.split('. ')
                    print(item)

                    for sentence in item:
                        words = sentence.replace('.', '').split(' ')

                        for w in words:
                            if (w != '') and (w not in '!@#$%^&*()[]{};:,./<>?\|`~-=_+'):
                                single_s.append(w)

                        sentences_l.append(single_s)
                        single_s = []

train_n = int(0.8 * len(sentences_l))
train_set = sentences_l[:train_n]
test_set = sentences_l[train_n:]

train_output = open('train.csv', 'w')
test_output = open('test.csv', 'w')

for element in train_set:
    train_output.write(str(element) + '\n')

for element in test_set:
    test_output.write(str(element) + '\n')

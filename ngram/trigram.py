import nltk
from nltk.corpus import stopwords

def generate_n_gram(words, n):
    temp = zip(*[words[i:] for i in range(0, n)])
    ans = [' '.join(n) for n in temp]
    return ans

def trigram_probability(body, Trigrams):
    trigram_pro_dict = {}

    for item in Trigrams:
        for each in item:
            bigram = ' '.join(each.split(' ')[0:2])
            last_word = each.split(' ')[2]
            count_tri = body.count(each)
            count_bi = body.count(bigram)

            if bigram not in trigram_pro_dict.keys():
                trigram_pro_dict[bigram] = {last_word: count_tri/count_bi}
            else:
                trigram_pro_dict[bigram][last_word] = count_tri/count_bi

    return trigram_pro_dict

Trigrams = []
sentence = []
# token_list = []
body = ''

train = open('train.csv', 'r')
content = train.readlines()[:1000]

for line in content:
    word_token = line.strip().split('\t')
    word = word_token[0]
    # token = word_token[1]

    if (not word.isdigit()) and word.isalpha():
        if word == "n't":
            word = 'not'

        if (word[0].isupper()) and bool(sentence):

            trigram = generate_n_gram(sentence, 3)
            Trigrams.append(trigram)

            sentence = []
            # token_list = []
            sentence.append(word.lower())
            # token_list.append(token)
            body += word.lower() + ' '
        else:
            sentence.append(word.lower())
            # token_list.append(token)
            body += word.lower() + ' '

trigram_prob = trigram_probability(body, Trigrams)

# print(trigram_prob)

####################################################predict sentence
def predict_sent(two_words, trigram_prob):
    predict = two_words
    probability = 0.3

    while probability >= 0.3:
        if two_words in trigram_prob.keys():
            probability = max(trigram_prob[two_words].values())
            print(probability)
            next_word = max(trigram_prob[two_words], key = trigram_prob[two_words].get)
            predict += ' ' + next_word
            print(predict)

            two_words = ' '.join(predict.split(' ')[-2:])
            print(two_words)
            continue
        else:
            predict += '.'
            break
    
    return predict

# two_words = input("Give me two words: ")
# predict = predict_sent(two_words, trigram_prob)

# print(predict)

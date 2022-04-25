import nltk
from nltk import pos_tag

def bigram_likeli_transi(POS, STATE):
    Likelihood = {}
    Transition = {}

    # Likelihood probability
    for i in POS:
        Likelihood[i] = POS[i]
        token_frequency = sum(Likelihood[i].values())
        for key, value in Likelihood[i].items():
            word_pro = float(value)/token_frequency
            Likelihood[i][key] = word_pro

    # all_tokens
    all_tokens = []
    all_tokens.append("Begin_Sent")
    for key in Likelihood:
        all_tokens.append(key)
    all_tokens.append("End_Sent")

    # transition probability
    for i in STATE:
        Transition[i] = STATE[i]
        frequencies = sum(Transition[i].values())
        for key, value in Transition[i].items():
            transi_pro = float(value)/frequencies
            Transition[i][key] = transi_pro

    return all_tokens, Likelihood, Transition

######################################################deal with data
POS = {}
STATE = {'Begin_Sent': {}, 'End_Sent': {}}

sentence = []
token_list = []

train = open('train.csv', 'r')
content = train.readlines()

for line in content[:1000]:
    try:
        word_token = line.split('\t')
        word = word_token[0]
        token = word_token[1]
    except:
        continue

    if word.isalpha():
        if (word[0].isupper()) and bool(sentence):

            sentence.append('.')
            token_list.append('.')

            #now a sentence is complete, store in POS
            for i in range(len(token_list)):
                t = token_list[i]
                w = sentence[i]

                if t not in POS.keys():
                    POS[t] = {w: 1}
                else:
                    if w not in POS[t].keys():
                        POS[t][w] = 1
                    else:
                        POS[t][w] += 1

            #store in STATE
            begin_token = token_list[0]
            if begin_token not in STATE['Begin_Sent'].keys():
                STATE['Begin_Sent'][begin_token] = 1
            else:
                STATE['Begin_Sent'][begin_token] += 1

            for i in range(len(token_list)-1):
                curr_t = token_list[i]
                next_t = token_list[i+1]

                if curr_t not in STATE.keys():
                    STATE[curr_t] = {next_t: 1}
                else:
                    if next_t not in STATE[curr_t].keys():
                        STATE[curr_t][next_t] = 1
                    else:
                        STATE[curr_t][next_t] += 1

            sentence = []
            token_list = []
            sentence.append(word.lower())
            token_list.append(token)
        else:
            sentence.append(word.lower())
            token_list.append(token)

STATE['End_Sent']['.'] = 1
train.close()

######################################################predict with bigram
all_tokens, Likelihood, Transition = bigram_likeli_transi(POS, STATE)

test_list = ["how are","please find below","I don't quite understand"]

for sentence in test_list:
    previous_word = sentence.split(" ")[-1]
    tag = nltk.pos_tag([previous_word])[0][-1]
    tag_dic = Transition.get(tag)
    max_tag = ""
    max_tag_pro = 0
    for key, value in tag_dic.items():
        if value > max_tag_pro:
            max_tag = key
            max_tag_pro = value
    probability = Likelihood.get(max_tag)
    max = 0
    predicted_word = ""
    suggestion_word = []
    for key, value in probability.items():
        if value > max:
            max = value
            predicted_word = key
            suggestion_word.append(predicted_word)
    # print("probability for ", sentence, " is:" , probability.get("innermost"))
    print("you previous sentence is ", sentence, "; your next word is ", predicted_word, " with a probability of ",max)
    print("here is your suggestion of words:", suggestion_word)
    print()
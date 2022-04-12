from nltk.translate.bleu_score import sentence_bleu 

sample_input = 'this is a dog'

reference = ['this is a dog'.split(),
            'it is dog'.split(),
             'dog it is'.split()]                 

candidate = 'it is dog'.split()

print('BLEU score -> {}'.format(sentence_bleu(reference,candidate)))
import os

directory = r'/Users/student/Desktop/maildir/cash-m/bankruptcy'
start = False
sentence_l = []

for root, subdirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.'):
            docs = open(os.path.join(root, file), 'r')
            content = docs.readlines()

            for item in content:
                if '. ' in item:
                    item = item.split('. ')
                    print(item)
        #     for item in docs.readlines():
        #         if
        #     for docs in txt:
        #         print(docs)
# file = open('/Users/student/Desktop/maildir/cash-m/bankruptcy', 'r')
#
# for each in file:
#     print(each)

perplexity
extract body part, n-gram, enron, 80% train, 20% test
by the weekend, get result from the enron data set.
a lot experiments, graphs, statisics
hpc? account?authorization?

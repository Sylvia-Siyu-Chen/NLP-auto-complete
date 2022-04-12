import os

directory = r'/Users/student/Desktop/maildir/cash-m/bankruptcy'

for root, subdirs, files in os.walk(directory):
    for file in files:
        print(file)
        # if file.endswith('.'):
        #     docs = open(os.path.join(root, file), 'r')
        #
        #     for i in range(2):
        #         print(docs.readline())
        #     for item in docs.readlines():
        #         if
        #     for docs in txt:
        #         print(docs)
# file = open('/Users/student/Desktop/maildir/cash-m/bankruptcy', 'r')
#
# for each in file:
#     print(each)

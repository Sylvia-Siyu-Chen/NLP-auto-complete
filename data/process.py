import email
from fileinput import filename
import imp
import os
from email.parser import Parser


rootdir = "/Users/sylv/Desktop/coding/NLP-auto-complete/maildir"
# subdir = "/Users/sylv/Desktop/coding/NLP-auto-complete/maildir/lay-k/family"

email_body = []

for dir, subdir, fnames in os.walk(rootdir):
    for name in subdir:
        sub = os.path.join(rootdir,name,"_sent_mail")
        # print(sub)
        for directory, subdirectory, filenames in  os.walk(sub):
            for filename in filenames:
                inputfile = os.path.join(directory,filename)
                with open(inputfile, "r") as f:
                    data = f.read()
                    email = Parser().parsestr(data)
                    email_body.append(email.get_payload())



total_sentences = []

for item in email_body:
    paragraph = item.split("\n")
    for sentences in paragraph:
        sentence = sentences.split(". ")
        for item in sentence:
            check = item.split(" ")
            if len(check)>1:
                total_sentences.append(item.strip(" "))


with open("train.csv","w") as w:
    for sentence in total_sentences:
        firstword = sentence.split(" ")[0]
        if (sentence != "") & (":" not in sentence) & ("@" not in sentence) &("---" not in sentence):
            w.write(sentence+"\n")
    w.close()
            


# email = Parser().parsestr(data)


# def email_analyse(inputfile, to_email_list, from_email_list, email_body):
#     with open(inputfile, "r") as f:
#         data = f.read()

#     email = Parser().parsestr(data)

#     to_email_list.append(email['to'])
#     from_email_list.append(email['from'])

#     email_body.append(email.get_payload())


# to_email_list = []
# from_email_list = []
# email_body = []

# for directory, subdirectory, filenames in  os.walk(rootdir):
#     for filename in filenames:
#         email_analyse(os.path.join(directory, filename), to_email_list, from_email_list, email_body )


# with open("to_email_list.txt", "w") as f:
#     for to_email in to_email_list:
#         if to_email:
#             f.write(to_email)
#             f.write("\n")

# with open("from_email_list.txt", "w") as f:
#     for from_email in from_email_list:
#         if from_email:
#             f.write(from_email)
#             f.write("\n")        

# with open("email_body.txt", "w") as f:
#     for email_bod in email_body:
#         if email_bod:
#             f.write(email_bod)
#             f.write("\n")     



# import os
# from email.parser import Parser
# rootdir = "/Users/sylv/Desktop/coding/NLP-auto-complete/maildir"


# def email_analyse(inputfile, to_email_list, from_email_list, email_body):
#     with open(inputfile, "r") as f:
#         data = f.read()

#     email = Parser().parsestr(data)

#     to_email_list.append(email['to'])
#     from_email_list.append(email['from'])

#     email_body.append(email.get_payload())


# to_email_list = []
# from_email_list = []
# email_body = []

# for directory, subdirectory, filenames in  os.walk(rootdir):
#     for filename in filenames:
#         email_analyse(os.path.join(directory, filename), to_email_list, from_email_list, email_body )


# with open("to_email_list.txt", "w") as f:
#     for to_email in to_email_list:
#         if to_email:
#             f.write(to_email)
#             f.write("\n")

# with open("from_email_list.txt", "w") as f:
#     for from_email in from_email_list:
#         if from_email:
#             f.write(from_email)
#             f.write("\n")        

# with open("email_body.txt", "w") as f:
#     for email_bod in email_body:
#         if email_bod:
#             f.write(email_bod)
#             f.write("\n")
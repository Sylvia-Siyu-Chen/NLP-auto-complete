# Email Auto-Complete Project 

### Team Member: 
- Paper Composition: James Jiang
- Programming and/or Software Development: [Sylvia Chen](https://github.com/Sylvia-Siyu-Chen) , Ning Yang
- theoretical issues (cs, math, linguistics): James Jiang, [Sylvia Chen](https://github.com/Sylvia-Siyu-Chen)
- Evaluation: Ning Yang, Shanshan Gong

### Problem Statement: 
Inspired by our school Gmail, which is able to auto-fill many common sentences when writing emails, we want to analyze different algorithms that are able to fulfill similar and even more profound functions in writing compositions of all kinds. We will set up evaluation metrics and run all models to find out what factors affect the correctness of soundness, semantics, and sentiments of the given texts the most. If time permits, we want to build up an algorithm that is able to give accurate autofill suggestions for replier, based on the context of sender’s email (i.e. if the mood of the email is negative, when the user is typing “I feel”, the algorithm will suggest to type “sorry about your”).


### Evaluation Plan 
We have three major targets to realize in our project: 
1. The first objective is to examine the soundness of auto-completed sentences, i.e. the composition of the sentence is correct;
2. The second objective is to check if the drafted email is semantically correct;
3. The third objective is to determine the correctness of the suggested tone of the message based on context’s sentiments.


### Academic Reference 
1. Dong-Ho Lee, Zhiqiang Hu, Roy Ka-Wei Lee. 2021. Improving Text Auto-Completion with Next Phrase Prediction. 
https://aclanthology.org/2021.findings-emnlp.378.pdf *ACL Anthology.*

    > This paper proposed a novel  intermediate training strategy called Next Phrase Prediction (NPP), and trained a T5-base model with NPP to solve the problem of huge fine-tuning efforts to perform domain-specific text auto-completion, including email domain. In our project, we can use the same data source from Enron email corpus to compare outputs using different base models like GPT-2 and NPP+T5. Also, we can use similar evaluation metrics like BLEU and SPICE. Like them, we consider to evaluate completed sentences in ways including soundness of the sentence, and the semantic similarity with the original sentence.


2. Stojan Trajanovski, Chad Atalla, Kunho Kim, Vipul Agarwal, Milad Shokouhi, Chris Quirk. 2021. When does text prediction benefit from additional context? An exploration of contextual signals for chat and email messages. https://aclanthology.org/2021.naacl-industry.1.pdf *ACL Anthology. *

    > This paper compares contextual text prediction algorithms in different large language models - chats and emails - based on two of the largest commercial platforms Microsoft Teams and Outlook. It thus drew conclusions on how contextual signals can contribute to prediction performance differently in different contexts. For example, on emails, time context is most beneficial with small relative gains of 2% over baseline. While in real-time chatting scenarios, using a tailored set of previous messages as context yields relative improvements over the baseline between 9.3% and 18.6% across various evaluation metrics. The method of evaluation and statistics about how different contextual factors influence prediction performance will come in handy when analyzing other text prediction algorithms.  

3. Yun-Nung Chen, Alexander I. Rudnicky. 2014. Two-Stage Stochastic Natural Language Generation for Email Synthesis by Modeling Sender Style and Topic Structure.
https://aclanthology.org/W14-4425.pdf *ACL Anthology*

    > This paper introduces a two-stage process for stochastic generation of email. In the first stage, it built sender-specific and topic-specific structure models according to structural label annotation which is defined in this project, and then, based on these two models, the paper predicted the sender-topic-specific mixture models by interpolation. In the second stage, the paper synthesized text content based on the particulars of an email element, and the goals of a given communication, which is also surface-level realization. This paper inspired us that we could also consider the sender style while auto-filling emails. At the same time, the tone of the completed sentences can be considered as an evaluation standard. Also, we plan to use the data from the Enron email dataset.


4. Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts. *2011. Learning Word Vectors for Sentiment Analysis.*
	https://aclanthology.org/P11-1015.pdf *ACL Anthology*
	
    > This article presents a model to capture both semantic and sentiment similarities among 
     words. The semantic component of the model learns word vectors via an unsupervised probabilistic model of documents. Additionally, the model has a supervised sentiment component that is capable of embracing many social and attitudinal aspects of meaning. 
    We found the Semantic and Sentiment Similarities model in the paper is useful for us to  analyze the overall tone of the email texts. The polarity dataset version 2.0 introduced by Pang and Lee (2004) is an ideal dataset to train our model, as it consists of 2,000 movie 
    reviews and is rich in sentimental expressions.

5. Chen, Mia Xu, et al. “Gmail Smart Compose.” Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, 2019, doi:10.1145/3292500.3330723. 

    > Their paper constructs a model that provides immediate context-dependent suggestions when writing emails, with a focus on latency, scale, privacy concerns, and metric design aspects. The authors explore 3 approaches to take advantage of contextual information, and they’ve decided to use Language Model A (LM-A) due to strict time constraints required for the project. LM-A uses a context encoder for encoding the subject and previous email body. That is then concatenated with the current email body to be used as input sequence for the language model. After running Transformation and RNN, the team has decided on the RNN model since while the Transformer based models have advantage in quality over RNN models, the average decoding latency is much worse. With a focus on personalization and concern for privacy, the team fine tuned their model with a n-gram language model. They also suggested a few possible improvements such as VAE to improve the control over text generation. 


### Strategy for problem solving
Our strategy is to firstly compare different modern text prediction algorithms under same evaluation metrics, concluding most determine contextual signals in email text scenarios. After evaluating different contextual signals and analyzing how they could contribute to text prediction performance, we plan to try different combinations of algorithms with highest ranking factors to improve prediction performance. We plan to use the corpus from the Enron Email Dataset, and evaluation metrics like BLEU, SPICE


### A collaboration plan
Our plan is to deal with one model for each group member, screen out the valuable factors and combine the test results into one integrated report. 
- *James* will be working on sentiment analysis, testing the sentiment model included in the article he read about. He will also construct our final research paper, gathering our experimental processes, results, and converting them into English, as well as the overall evaluation. 

- *Ning* will work on training base models like NPP+T5 and GPT-2, and evaluate the outputs in three ways as mentioned above: soundness, semantic similarity and sentimental correctness. She will also compare these results with other team members’ results, and collaborate with them to find out the most competing features, and possible improvements of auto-fill algorithms.

- *Sylvia* will be working on collecting different modern text prediction algorithms, analyzing contextual signals, concluding ranking of factors, and putting together the final improved algorithm. She will be responsible for major code writing and running of data. 

- *Shanshan* will mainly be responsible for evaluating outputs of models using Log Perplexity method, ExactMatch@N, and Final prediction probability. Log perplexity is a typical measurement for language model evaluation that determines how well a model fits the data. The lower the perplexity, the better the predictions; ExactMatch@N measures how well a model performs at different suggestion length (N). Their paper also includes a weighted average for all lengths up to N=15; Final prediction probability will concern privacy and personalization concerns to find an optimized balance between “global” results and “personal” results. 

# python
from itertools import chain
import math

import os

# pypi
from dotenv import load_dotenv
from expects import be_true, equal, expect
import csv 
# this project

import modulefinder

from ngram.Ngram import NGrams 

# load_dotenv("posts/nlp/.env", override=True)


# path = os.environ["train.csv"]

file = open("/Users/sylv/Desktop/coding/NLP-auto-complete/data/train.csv", "r")
csv_reader = csv.reader(file)

lists_from_csv = []
vocabulary = []
for row in csv_reader:
    lists_from_csv.append(row)
    for word in row:
        vocabulary.append(word.strip("\n./\}{+-?><!@#$,%^&*()~`"))

# print(lists_from_csv)


def estimate_probability(word,
                         previous_n_gram,
                         n_gram_counts,
                         n_plus1_gram_counts,
                         vocabulary_size,
                         k) :
    """
    Estimate the probabilities of a next word using the n-gram counts with k-smoothing

    Args:
       word: next word
       previous_n_gram: A sequence of words of length n
       n_gram_counts: Dictionary of counts of n-grams
       n_plus1_gram_counts: Dictionary of counts of (n+1)-grams
       vocabulary_size: number of words in the vocabulary
       k: positive constant, smoothing parameter

    Returns:
       A probability
    """
    previous_n_gram = tuple(previous_n_gram)
    previous_n_gram_count = n_gram_counts.get(previous_n_gram, 0)

    n_plus1_gram = previous_n_gram + (word,)  
    n_plus1_gram_count = n_plus1_gram_counts.get(n_plus1_gram, 0)       
    return (n_plus1_gram_count + k)/(previous_n_gram_count + k * vocabulary_size)


def estimate_probabilities(previous_n_gram, n_gram_counts, n_plus1_gram_counts, vocabulary, k=1.0):
    """
    Estimate the probabilities of next words using the n-gram counts with k-smoothing

    Args:
       previous_n_gram: A sequence of words of length n
       n_gram_counts: Dictionary of counts of (n+1)-grams
       n_plus1_gram_counts: Dictionary of counts of (n+1)-grams
       vocabulary: List of words
       k: positive constant, smoothing parameter

    Returns:
       A dictionary mapping from next words to the probability.
    """

    # convert list to tuple to use it as a dictionary key
    previous_n_gram = tuple(previous_n_gram)

    # add <e> <unk> to the vocabulary
    # <s> is not needed since it should not appear as the next word
    vocabulary = vocabulary + ["<e>", "<unk>"]
    vocabulary_size = len(vocabulary)

    probabilities = {}
    for word in vocabulary:
        probability = estimate_probability(word, previous_n_gram, 
                                           n_gram_counts, n_plus1_gram_counts, 
                                           vocabulary_size, k=k)
        probabilities[word] = probability

    return probabilities

# UNQ_C11 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: suggest_a_word
def suggest_a_word(previous_tokens, n_gram_counts, n_plus1_gram_counts, vocabulary, k=1.0, start_with=None):
    """
    Get suggestion for the next word

    Args:
       previous_tokens: The sentence you input where each token is a word. Must have length > n 
       n_gram_counts: Dictionary of counts of (n+1)-grams
       n_plus1_gram_counts: Dictionary of counts of (n+1)-grams
       vocabulary: List of words
       k: positive constant, smoothing parameter
       start_with: If not None, specifies the first few letters of the next word

    Returns:
       A tuple of 
         - string of the most likely next word
         - corresponding probability
    """

    # length of previous words
    n = len(list(n_gram_counts.keys())[0]) 

    # From the words that the user already typed
    # get the most recent 'n' words as the previous n-gram
    previous_n_gram = previous_tokens[-n:]

    # Estimate the probabilities that each word in the vocabulary
    # is the next word,
    # given the previous n-gram, the dictionary of n-gram counts,
    # the dictionary of n plus 1 gram counts, and the smoothing constant
    probabilities = estimate_probabilities(previous_n_gram,
                                           n_gram_counts, n_plus1_gram_counts,
                                           vocabulary, k=k)

    # Initialize suggested word to None
    # This will be set to the word with highest probability
    suggestion = None

    # Initialize the highest word probability to 0
    # this will be set to the highest probability 
    # of all words to be suggested
    max_prob = 0

    ### START CODE HERE (Replace instances of 'None' with your code) ###

    # For each word and its probability in the probabilities dictionary:
    for word, prob in probabilities.items(): # complete this line

        # If the optional start_with string is set
        if start_with is not None: # complete this line

            # Check if the beginning of word does not match with the letters in 'start_with'
            if not word.startswith(start_with): # complete this line

                # if they don't match, skip this word (move onto the next word)
                continue # complete this line

        # Check if this word's probability
        # is greater than the current maximum probability
        if prob > max_prob: # complete this line

            # If so, save this word as the best suggestion (so far)
            suggestion = word

            # Save the new maximum probability
            max_prob = prob

    ### END CODE HERE

    return suggestion, max_prob





unique_words = list(set(vocabulary))

print(unique_words)

unigram_counts = NGrams(data=lists_from_csv, n=1).counts
bigram_counts = NGrams(data=lists_from_csv,n=2).counts

previous_tokens = ["how", "are"]
word, probability = suggest_a_word(previous_tokens, unigram_counts, bigram_counts, unique_words, k=1.0)
print(f"The previous words are {previous_tokens},\n\tand the suggested word is `{word}` with a probability of {probability:.4f}")

# expected_word, expected_probability = "a", 0.2727
# expect(word).to(equal(expected_word))
# expect(math.isclose(probability, expected_probability, abs_tol=1e-4)).to(be_true)
print()

# test your code when setting the starts_with

# tmp_starts_with = 'c'
# word, probability = suggest_a_word(previous_tokens, unigram_counts, bigram_counts, unique_words, k=1.0, start_with=tmp_starts_with)
# print(f"The previous words are 'i like', the suggestion must start with `{tmp_starts_with}`\n\tand the suggested word is `{word}` with a probability of {probability:.4f}")

# expected_word, expected_probability = "cat", 0.0909
# expect(word).to(equal(expected_word))
# expect(math.isclose(probability, expected_probability, abs_tol=1e-4)).to(be_true)


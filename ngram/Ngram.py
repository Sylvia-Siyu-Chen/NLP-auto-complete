# python
from collections import Counter
from itertools import chain

# pypi
import attr


@attr.s(auto_attribs=True)
class NGrams:
    """The N-Gram Language Model

    Args:
     data: the training data
     n: the size of the n-grams
     start_token: string to represent the start of a sentence
     end_token: string to represent the end of a sentence
    """
    data: list
    n: int
    start_token: str="<s>"
    end_token: str="<e>"
    _start_tokens: list=None
    _end_tokens: list=None
    _sentences: list=None
    _n_grams: list=None
    _counts: dict=None

    @property
    def end_tokens(self) -> list:
        """List of 1 end-tokens"""
        if self._end_tokens is None:
            self._end_tokens = [self.end_token]
        return self._end_tokens

    @property
    def start_tokens(self) -> list:
        """List of 'n' start tokens"""
        if self._start_tokens is None:
            self._start_tokens = [self.start_token] * self.n
        return self._start_tokens

    @property
    def sentences(self) -> list:
        """The data augmented with tags and converted to tuples"""
        if self._sentences is None:
            self._sentences = [tuple(self.start_tokens + sentence + self.end_tokens)
                            for sentence in self.data]
        return self._sentences

    @property
    def n_grams(self) -> list:
        """The n-grams from the data

        Warning:
        this flattens the n-grams so there isn't any sentence structure
        """
        if self._n_grams is None:
            self._n_grams = chain.from_iterable([
                [sentence[cut: cut + self.n] for cut in range(0, len(sentence) - (self.n - 1))]
                for sentence in self.sentences
            ])
        return self._n_grams

    @property
    def counts(self) -> Counter:    
        """A count of all n-grams in the data

        Returns:
        A dictionary that maps a tuple of n-words to its frequency
        """
        if self._counts is None:        
            self._counts = Counter(self.n_grams)
        return self._counts
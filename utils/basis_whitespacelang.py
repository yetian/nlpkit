'''
    basic functions for analyzing NLP with whitespace splitted languages
    using nltk
    input: str
'''
import nltk
from nltk.tokenize import RegexpTokenizer

class basis_wsl(object):

    def word_freq(self, text, case_sensitive=True):

        text = text.strip()

        if text == '':
            return ''

        if case_sensitive == False:
            text = text.lower()

        tokenizer = RegexpTokenizer(r'\w+')
        text_tokens = tokenizer.tokenize(text)



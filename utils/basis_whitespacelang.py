'''
    basic functions for analyzing NLP with whitespace splitted languages
    using nltk
    input: str
'''
import nltk
from nltk.tokenize import RegexpTokenizer

class basis_wsl(object):

    # by assumption text is a sentence.
    # to do sentence tokenization, use nltk's sent_tokenize
    def word_freq(self, text, case_sensitive=True, return_tuple=False):

        text = text.strip()

        if text == '':
            return ''

        if case_sensitive == False:
            text = text.lower()

        tokenizer = RegexpTokenizer(r"[\w']+")
        text_tokens = tokenizer.tokenize(text)

        tokens_freq = {}

        for token in text_tokens:
            if token not in tokens_freq.keys():
                tokens_freq[token] = 1
            else:
                tokens_freq[token] += 1

        if return_tuple == True:
            return tuple(tokens_freq.items())
        return tokens_freq


#test
bwsl = basis_wsl()
text = "You can do it. You can't do it. Sie könnten es machen. Buenos dias. Adiós."
print (bwsl.word_freq(text, False, True))

from Text_Summary import Summary
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer

class Final_Summary:
    def Get_Summary():
        file = open('../transcripts/transcript.txt', 'r')
        text = file.read()
        freq_table = Summary.create_frequency_table(text)

        '''
        We already have a sentence tokenizer, so we just need 
        to run the sent_tokenize() method to create the array of sentences.
        '''

        # 2 Tokenize the sentences
        sentences = sent_tokenize(text)

        # 3 Important Algorithm: score the sentences
        sentence_scores = Summary.score_sentences(sentences, freq_table)

        # 4 Find the threshold
        threshold = Summary.find_average_score(sentence_scores)

        # 5 Important Algorithm: Generate the summary
        summary = Summary.generate_summary(sentences, sentence_scores, 1.5 * threshold)

        return summary

import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# from transformers import BertTokenizer, BertModel
import numpy as np
# import torch  # Import PyTorch
from collections import Counter

class NLPIntegration:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.nlp = spacy.load("en_core_web_sm")

    def tokenize_text(self, text):
        return word_tokenize(text)

    def remove_stopwords(self, tokens):
        stop_words = set(stopwords.words("english"))
        return [word for word in tokens if word.lower() not in stop_words]

    def analyze_sentiment(self, text):
        sentiment_scores = self.sia.polarity_scores(text)
        return sentiment_scores

    def named_entity_recognition(self, text):
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities
    
    def identify_search_topic(self, query):
    # Process the query using spaCy
        doc = self.nlp(query)

        # Extract nouns and proper nouns as potential topics
        nouns = [token.text for token in doc if token.pos_ in ("NOUN", "PROPN")]

        # Create a frequency count of the extracted keywords
        keyword_counts = Counter(nouns)

        # Find the most frequent keyword as the search topic
        if keyword_counts:
            search_topic = keyword_counts.most_common(1)[0][0]
            return search_topic
        else:
            return "No specific topic identified"

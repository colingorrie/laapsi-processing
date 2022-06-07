from cltk import NLP
from cltk.lemmatize.ang import OldEnglishDictionaryLemmatizer
from cltk.phonology.ang.transcription import Word

cltk_nlp = NLP(language="ang")


class OldEnglishLemmatizer:

    def __init__(self):
        self.lemmatizer = OldEnglishDictionaryLemmatizer()

    def lemmatize(self, token):
        word = Word(token).remove_diacritics()
        return self.lemmatizer.lemmatize_token(word)

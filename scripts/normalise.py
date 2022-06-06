from enum import Flag, auto


class Norm(Flag):
    UNCHANGED = 0
    CAPITALISED = auto()
    ALL = (CAPITALISED)


class OldEnglishNormaliser:

    def __init__(self, config=Norm.ALL, proper_nouns=set()):
        self.config = config
        self.proper_nouns = proper_nouns

    def normalise(self, token):

        norm = token
        norm_code = Norm.UNCHANGED

        if self.config & Norm.CAPITALISED:
            if norm not in self.proper_nouns:
                if norm != norm.lower():
                    norm = norm.lower()
                    norm_code |= Norm.CAPITALISED

        return norm, norm_code

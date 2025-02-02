#!/usr/bin/env python3

from collections import defaultdict
import unicodedata

from greek_accentuation.characters import strip_length
import yaml

from src.cltk_integration import OldEnglishLemmatizer
from src.constants import N_CHAPTERS, TEXT_NAME
from src.morpheus import Morpheus
from src.utils import print_interlinear


def lemmatise():
    try:
        with open("manual-data/lemma_overrides.yaml") as f:
            lemma_overrides = yaml.safe_load(f)
    except FileNotFoundError:
        lemma_overrides = {}

    lemmatizer = OldEnglishLemmatizer()

    problems = defaultdict(list)

    with Morpheus("cache/morpheus.json") as morpheus:

        for chapter_num in range(1, N_CHAPTERS + 1):
            input_filename = f"analysis/{TEXT_NAME}.sent.{chapter_num:03d}.norm.txt"
            output_filename = f"analysis/{TEXT_NAME}.sent.{chapter_num:03d}.lemma.txt"

            with open(input_filename) as f, open(output_filename, "w") as g:
                for line in f:
                    if ".text" in line:
                        text_list = line.strip().split()
                    if ".flags" in line:
                        flags_list = line.strip().split()
                    if ".norm" in line:
                        ref = line.split(".norm")[0]
                        norm_list = line.strip().split()
                        lemma_list = [f"{ref}.lemma"]

                        for norm in line.split()[1:]:

                            # see if we have an override

                            lemma = None
                            prefix = None
                            if norm in lemma_overrides:
                                lemma = lemma_overrides[norm].get("default")
                                for k, v in lemma_overrides[norm].items():
                                    if not isinstance(k, str):
                                        print(
                                            f"*** {k} is not a string (under {norm})"
                                        )
                                        break
                                    if k != "default" and ref.startswith(k):
                                        if prefix is None or len(k) > len(
                                                prefix):
                                            prefix = k
                                            lemma = v

                            # otherwise check morpheus

                            if lemma is None:
                                lemmas = []
                                result = lemmatizer.lemmatize(
                                    strip_length(norm))
                                if result:
                                    lemmas.append(result)
                                if len(lemmas) != 1:
                                    problems[(norm, "|".join(
                                        sorted(lemmas)))].append(ref)
                                    lemma = "-"
                                else:
                                    lemma = lemmas[0]
                            lemma_list.append(lemma)

                        print_interlinear(
                            [text_list, norm_list, flags_list, lemma_list], g)

    for norm, lemmas in problems.keys():
        print(norm, lemmas.split("|"), problems[(norm, lemmas)])

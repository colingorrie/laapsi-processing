#!/usr/bin/env python3
"""
converts the textpart-per-paragraph to textpart-per-sentence.
"""

from tkinter.tix import TEXT
from constants import N_CHAPTERS, TEXT_NAME
from utils import print_interlinear

from greek_normalisation.normalise import Normaliser, Norm

config = (Norm.CAPITALISED)
proper_nouns = set([
    "Engla-land", "Engla-lande", "Osweald", "Wintanceaster", "Wintanceastre",
    "Æþelrǣd", "Ælfgiefu", "Ælfgiefe"
])


def format_flags(flags):
    s = ""
    if flags & Norm.CAPITALISED:
        s += "c"

    if s == "":
        s = "."

    return s


normalise = Normaliser(config, proper_nouns).normalise

for chapter_num in range(1, N_CHAPTERS + 1):
    input_filename = f"text/{TEXT_NAME}.sent.{chapter_num:03d}.txt"
    output_filename = f"analysis/{TEXT_NAME}.sent.{chapter_num:03d}.norm.txt"

    with open(input_filename) as f, open(output_filename, "w") as g:
        for line in f:
            line = line.strip()
            ref, *text = line.split()
            text_list = [f"{ref}.text", *text]
            norm = [f"{ref}.norm"]
            flags = [f"{ref}.flags"]
            for token in text:
                norm_token, norm_flags = normalise(token.strip(",.;·«»()!?"))
                norm.append(norm_token)
                flags.append(format_flags(norm_flags))

            print_interlinear([text_list, flags, norm], g)

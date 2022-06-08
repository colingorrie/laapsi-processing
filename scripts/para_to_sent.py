#!/usr/bin/env python3
"""
converts the textpart-per-paragraph to textpart-per-sentence.
"""

from src.constants import N_CHAPTERS, TEXT_NAME


def para_to_sent():
    for chapter_num in range(1, N_CHAPTERS + 1):
        input_filename = f"text/{TEXT_NAME}.para.{chapter_num:03d}.txt"
        output_filename = f"text/{TEXT_NAME}.sent.{chapter_num:03d}.txt"

        with open(input_filename) as f, open(output_filename, "w") as g:
            for line in f:
                line = line.strip()
                ref, text = line.split(maxsplit=1)
                if ref.endswith(".00"):  # ignore headings
                    continue
                sentence = []
                sent_num = 1
                for token in text.split():
                    sentence.append(token)
                    if "." in token or ";" in token or "·" in token or "!" in token:
                        print(f"{ref}.{sent_num} {' '.join(sentence)}", file=g)
                        sent_num += 1
                        sentence = []
            assert sentence == [], f"finished para {ref} mid-sentence"

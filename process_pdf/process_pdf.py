import pandas as pd

df = pd.read_csv("vocab_list.csv")

pos_map = {
    "preposition": "prep.",
    "noun": "n.",
    "verb": "v.",
    "adjective": "adj.",
    "adverb": "adv.",
    "conjunction": "conj.",
    "enclitic": "enclitic",
    "pronoun": "pron.",
    "noun (proper)": "proper n.",
    "interjection": "interj."
}

df["Definition"] = "(" + df["Part of Speech"].map(pos_map) +")" + " " + df["Definition"]

df = df[["Vocabulary", "Definition"]]

df.to_csv("../sets/latin.csv", index=False)

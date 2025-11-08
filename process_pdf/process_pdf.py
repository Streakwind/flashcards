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

def map_pos(pos_string):
    if pd.isna(pos_string):
        return ""
    parts = [p.strip().lower() for p in pos_string.split("/")]
    mapped = [pos_map.get(p, p) for p in parts]
    return "/".join(mapped)

df["Definition"] = "(" + df["Part of Speech"].apply(map_pos) + ") " + df["Definition"]

df = df[["Vocabulary", "Definition"]]

df.to_csv("../sets/latin.csv", index=False)
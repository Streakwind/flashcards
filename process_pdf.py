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
}

if (df["Part of Speech"].map(pos_map) is not None):
    df["Definition"] = "(" + df["Part of Speech"].map(pos_map) +")" + " " + df["Definition"]
else:
    raise ValueError(f"""Unknown part of speech found: {df["Part of Speech"]}""")

df = df[["Vocabulary", "Definition"]]

df.to_csv("vocab_final.csv", index=False)

print(df.head())

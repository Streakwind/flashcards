import pandas as pd

csv_path = "../sets/latin.csv"

df = pd.read_csv(csv_path)

# test with aether, -eris which splits between lines
vocab = df.loc[27, "Vocabulary"]
print(repr(vocab))

df["Vocabulary"] = df["Vocabulary"].str.replace(r"[\r\n]+", " ", regex=True)

vocab = df.loc[27, "Vocabulary"]
print(repr(vocab))

df.to_csv(csv_path, index=False)
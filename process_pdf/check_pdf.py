import pandas as pd

csv_path = "../sets/latin.csv"

df = pd.read_csv(csv_path)

df["Vocabulary"] = df["Vocabulary"].str.replace(r"[\r\n]+", " ", regex=True)
df["Definition"] = df["Definition"].str.replace(r"[\r\n]+", " ", regex=True)

df.to_csv(csv_path, index=False)
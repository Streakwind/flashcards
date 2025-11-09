import pandas as pd
import random
import os

df = pd.read_csv("latin.tsv", sep="\t")

words = list(df.itertuples(index=False, name=None))  # list of (vocab, definition)

random.shuffle(words)

chunks = [words[i:i + 50] for i in range(0, len(words), 50)]

output_dir = "../sets/batches"
os.makedirs(output_dir, exist_ok=True)

for i, chunk in enumerate(chunks):
    batch_df = pd.DataFrame(chunk, columns=["Vocabulary", "Definition"])
    batch_filename = os.path.join(output_dir, f"batch{i+1}.tsv")
    batch_df.to_csv(batch_filename, sep="\t", index=False)
    print(f"Saved {batch_filename} ({len(chunk)} words)")

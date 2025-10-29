import pandas as pd

topic = input("what would you like to study? ")

df = pd.read_csv(f"sets/{topic}.csv")

cards = df.sample(frac=1).reset_index(drop=True)\

for _, row in cards.iterrows():
    word = row["Vocabulary"]
    definition = row["Definition"]

    user_input = input(f"{word}: ")
    if user_input.lower() == "q":
        break

    if definition.startswith("("):
        definition = definition.split(")", 1)[1].strip()
        
    possible = str.split(definition, ", ")

    if user_input not in possible:
        print("Incorrect")
    else:
        print("Correct")
        
    print(f"Definition: {definition}\n")
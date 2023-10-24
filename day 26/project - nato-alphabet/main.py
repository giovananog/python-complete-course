import pandas

data = pandas.read_csv("NATO-alphabet-start\\nato_phonetic_alphabet.csv")


new_data = {b.letter:b.code for (a,b) in data.iterrows()}

# user_name = input("type a name you want to know the exactly spell: ")

user_name = "joao"

print([new_data[b.upper()] for b in user_name])


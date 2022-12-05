import pandas

# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user = input("Enter a name: ").upper()
user_list = [letter.upper() for letter in user]
new_list = [new_dict[letter] for letter in user if letter in new_dict]
print(new_list)

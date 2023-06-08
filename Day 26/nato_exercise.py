import pandas

nato_words_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_words_df.iterrows()}
# print(nato_dict)

word = input("Enter a word: ").upper()
cipher_list = [nato_dict[letter] for letter in word]
print(cipher_list)

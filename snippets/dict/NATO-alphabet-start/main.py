import pandas
df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}
input = input("Write something: ").upper()
nato_list = [nato_dict[letter] for letter in input ]
print(nato_list)
print("END")
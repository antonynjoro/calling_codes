student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(key,value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
letter_data = pandas.read_csv('nato_phonetic_alphabet.csv')

dictionary = {data['letter']:data['code'] for (index,data) in letter_data.iterrows()}

name = input("What is your name? ")

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
code_name = [dictionary[letter.upper()]+" " for letter in name]

code_name_string = "".join(code_name)

print (f"Your Code Name is: {code_name_string}")

import string

input_string =input("Choise letter:")
start_letter , end_letter = input_string.split('-')
start_index = string.ascii_letters.index(start_letter)
end_index = string.ascii_letters.index(end_letter)
result = string.ascii_letters[start_index:end_index + 1]
print(result)

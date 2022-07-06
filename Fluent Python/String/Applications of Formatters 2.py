# Using a dictionary for string formatting: 

# Use a dictionary to unpack values into the placeholders in the string that needs to be formatted. 
# We basically use ** to unpack the values. 
# This method can be useful in string substitution while preparing an SQL query.

intro = 'My name is {first_name} {middle_name} {last_name} aka the {aka}.'
full_name = {
    'first_name': 'Tony', 
    'middle_name': 'Howard', 
    'last_name': 'Stark', 
    'aka': 'Iron Man'
}

# tham chieu thang tu keys den values luon: key la keyword name, value la gia tri can dien.
print(intro.format(**full_name))   # use ** to unpack the values







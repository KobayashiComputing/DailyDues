import json

# Set up the dictionaries
settings_from_code = {"name": None, "age": None, "city": None, "lastname": None}

settings_from_db = {'name': 'Alice', 'age': 25, 'city': 'New York'}
string_from_db = json.dumps(settings_from_db)
settings_from_db = json.loads(string_from_db)

# use the 'update()' method to update one dictionary with items from the other
settings_from_code.update(settings_from_db)

# now we can use 'settings_from_code' in the code with the appropriate values 
# from the database, and new items with the default values
print(settings_from_code)

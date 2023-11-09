#!/usr/bin/python3
import sys
from your_module import save_to_json_file, load_from_json_file
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

"""Get the command line arguments excluding the script name"""
arguments = sys.argv[1:]
"""Load existing data from the file if it exists"""
try:
    existing_data = load_from_json_file('add_item.json')
except FileNotFoundError:
    existing_data = []

# Add the new arguments to the existing data
existing_data.extend(arguments)

# Save the updated data to the file
save_to_json_file(existing_data, 'add_item.json')

print("Arguments have been added to 'add_item.json'.")


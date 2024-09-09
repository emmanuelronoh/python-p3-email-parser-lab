# lib/email_address_parser.py

import re

class EmailAddressParser:
    def __init__(self, input_string):
        # Initialize with the input string
        self.input_string = input_string
    
    def parse(self):
        # Define a regular expression to match email addresses
        email_regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
        
        # Find all matches in the input string
        matches = email_regex.findall(self.input_string)
        
        # Remove duplicates and return in reverse order of appearance
        return list(dict.fromkeys(matches).keys())[::-1]

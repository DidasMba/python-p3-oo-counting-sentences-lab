#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the string using periods, question marks, and exclamation marks as separators
        sentences = re.split(r'[.!?]', self.value)

        # Filter out empty strings from the list
        sentences = list(filter(lambda sentence: sentence.strip() != '', sentences))

        return len(sentences)
    
    
    


#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ""):
      self._value = value

    @property
    def value(self):
      return self._value

    @value.setter
    def value(self, new_value):
      if not isinstance(new_value, str):
        print("The value must be a string.")
      else:
        self._value = new_value

    def is_sentence(self):
      if self._value is None:
        return False
      return self._value.endswith(".")

    def is_question(self):
      if self._value is None:
        return False
      else:
        return self._value.endswith("?")

    def is_exclamation(self):
      if self._value is None:
        return False
      else:
        return self._value.endswith("!")

    def count_sentences(self):
      if self._value is None:
        return 0
      
      modified_value = self._value.replace(".", "#").replace("!", "#").replace("?", "#")

      # Split the modified string using the unique character as the separator
      sentences = modified_value.split("#")

      # Remove empty strings from the result of split
      sentences = [sentence for sentence in sentences if sentence]

      return len(sentences)


my_string_instance = MyString()        
my_string_instance.value = "Hello!"
print(my_string_instance.value)
print(my_string_instance.is_sentence())
print(my_string_instance.is_question())
#!/usr/bin/env python3
import re
class MyString:
  
  def __init__(self, value = ""):
    self._value = value
    
  def get_value(self):
    return self._value

  def set_value(self, stringVal):
    if (type(stringVal) == str):
      self._value = stringVal
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

#   def __init__(self, value=""):
#           self.value = value
   
#   def get_value(self):
#     return self._value

#   def checking_string(self, value):
#        if not isinstance(value, str):
#             print("The value must be a string.")
#        else:
#             self._value = value

#   value = property(get_value, checking_string)

  def is_sentence(self):
     return self.value.endswith(".")

  def is_question(self):
     return self.value.endswith("?")
  
  def is_exclamation(self):
     return self.value.endswith("!")
  
  def count_sentences(self):
           pattern = r"[.?!]+"
           sentences = re.findall(pattern, self.value)
           return len(sentences)
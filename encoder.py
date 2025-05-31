from message import Message

# number to word methods
from num2words import num2words
# string manipulation methods
import string as s
# reg-ex methods
import re

class Encoder:
  def __init__(self, message: Message):
    assert type(message) == Message, 'Message is not a Message object'
    self.__message = message
  
  def encode_message(self):
    clean_string = Encoder.remove_punctuation(self.__numbers_to_words())
    return Encoder.convert_to_hex(clean_string)
  
  def decode_message(self):
    encoded_list = list(self.__message.message.split(" "))
    char_list = Encoder.hex_to_char(encoded_list)
    
    return "".join(char_list)
  
  def __numbers_to_words(self):
    numbers = re.findall(r'\d+', self.__message.message)
    text = self.__message.message
    
    for number in numbers:
      text = text.replace(str(number), num2words(int(number))) 
    
    return text
  
  @staticmethod
  def remove_punctuation(string: str):
    assert type(string) == str, 'The arguement given is not of type string'
    assert len(string) > 0, 'The arguement given is an empty string'
    
    # replace hyphens with spaces
    string = string.replace("-", " ")

    # remove all other punctuation
    for char in string:
      if char in s.punctuation:
        string = string.replace(char, "")

    # remove all spaces
    string = string.replace(" ", "")
    
    return string
  
  @staticmethod
  def convert_to_hex(string: str):
    assert type(string) == str, 'The arguement given is not of type string'
    assert len(string) > 0, 'The arguement given is an empty string'
    
    hex_string = ""
    
    for i, char in enumerate(string):
      if i != len(string) -1:
        hex_string = hex_string + hex(ord(char))[2:] + " "
      else:
        hex_string = hex_string + hex(ord(char))[2:]
    
    return hex_string

  @staticmethod
  def hex_to_char(list: list):
    assert type(list) == list, 'The arguement given is not of type list'
    
    ord_list = []
    
    for item in list:
      ord_list.append(chr(int(item, 16)))
  
    return ord_list